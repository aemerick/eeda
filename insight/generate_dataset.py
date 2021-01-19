"""
   author: A. Emerick

   Script to generate a dataset that can be easily loaded with numpy or Pandas
   of star particle abundance data for demonstration purpses.

"""
import numpy as np
import gizmo_analysis as ga

FIRE_elements = ['H','He','C','N','O','Ne','Mg','Si','S','Ca','Fe']

def load_dataset(model_name,  z=0.01, index=600, wdir = './input/m11i_res7100/'):
    """
    Wrapper around gizmo_analysis's data reading
    `gizmo_analysis.io.Read.read_snapshots` method to also layer on necessary
    set-up for the age-tracers, using either the FIRE2 default yield model
    or the NuGrid yield model at the specific metal mass fraction (`z`).
    """

    # load the 0th data set and set initial abundances
    part0 = ga.io.Read.read_snapshots(['gas'],'index',0,simulation_directory=wdir)
    initial = {}
    for e in FIRE_elements:
        initial[str.lower(e)] = np.average(part0['gas'].prop('massfraction.' + str.lower(e)))
    initial['metals'] = np.average(part0['gas'].prop('massfraction.metals'))


    # load the last snapshot
    part = ga.io.Read.read_snapshots(['star'], 'index', index, simulation_directory=wdir)

    if model_name == "FIRE":
        z_solar_fire = 0.02

        model = ga.agetracers.FIRE2_yields(model_Z = z / z_solar_fire, Z_scaling=True)
    elif model_name == "NuGrid":
        sygma_kwargs = {'imf_type' : 'kroupa', 'dt':1e4, 'special_timesteps':1000,
                      'ns_merger_on':True,'imf_bdys':[0.1,100.01],'tend':1.5e10,'f_binary':1.0,
                      'transitionmass':8.0,'imf_yields_range':[1,99.0]}

        model = ga.agetracers.NuGrid_yields(iniZ=z, **sygma_kwargs)

    yield_table = ga.agetracers.construct_yield_table(model, part.ageprop.age_bins/1000.0)

    part.set_yield_table(yield_table, [str.lower(x) for x in model.elements])
    part.set_initial_abundances(initial)

    return part


def save_star_data(part, outname, agetracers=False):
    """
    Save star particle data into a text file.
    """

    dataset = {}
    fields = {'mass':'mass', 'mass.form' : 'mass_form', 'age':'age', 'form.time':'formation'}
    for k in fields.keys():
        dataset[fields[k]] = part['star'].prop(k)

    if agetracers:
        agetracer_string = 'agetracer.'
    else:
        agetracer_string = ''

    for e in FIRE_elements:
        if e == 'h' or e == 'H':
            continue

        e = str.lower(e)
        dataset[e + '_over_h'] = part['star'].prop('metallicity.' + agetracer_string + e)

    for (e1,e2) in [('mg','fe'),('c','fe'),('o','fe'),('c','mg'),('o','mg'),('o','n'),('si','fe')]:
        if e1 == e2:
            continue

        e1 = str.lower(e1)
        e2 = str.lower(e2)

        dataset[e1 + '_over_' + e2] = part['star'].prop('metallicity.' + agetracer_string + e1) -\
                                      part['star'].prop('metallicity.' + agetracer_string + e2)



    f = open(outname,'w')
    _dummy = [f.write(k + ' ') for k in dataset.keys()]
    f.write("\n")
    for i in np.arange(np.size(dataset['mass'])):
        for k in dataset.keys(): #['mass','mass_form','age','formation']:
            if '_over_' in k:
                f.write("%6.3f "%(dataset[k][i]))
            else:
                f.write("%.4E "%(dataset[k][i]))
        f.write("\n")

    f.close()

    return

if __name__ == "__main__":

    part_fire = load_dataset("FIRE")
    save_star_data(part_fire, "./input/m11i_fire2_abundances.dat", agetracers=False)
    save_star_data(part_fire, "./input/m11i_fire2_AT_abundances.dat", agetracers=True)

    part_nugrid = load_dataset("NuGrid")
    save_star_data(part_nugrid, "./input/m11i_NuGird_AT_abundances.dat", agetracers=True)
