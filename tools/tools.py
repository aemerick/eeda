"""
 Collection of useful tools that I WILL move somewhere
 more sensible once this gets long (e.g. its own package)
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_categorical(xvar, 
                     yvar, 
                     rfunction,
                     categories=None,
                     data=None,
                     ax = None):
    """
    Plot some reduction function of yvar for each category
    of xvar. This can be used, for example, to compute
    the mean by passing 'np.mean' as `rfunction`,
    or more complex things like computing the fraction
    of points in each bin with some condition on yvar:
    
    Example, fraction of each points with associated y's
    > 10 could be done with passing:
    
        rfunction = lambda u : np.sum(u>10) / len(u)
    
    Parameters:
    ------------
    
    xvar      : np.array of x values OR valid key
                in data.
    yvar      : np.array of y values OR valid key
                in data.
    rfunction : a function that accepts an array
                and returns a single value. 
    categories: Optional. If provided, the list of categories
                in xvar to compute statistic for. Otherwise
                uses all unique categories in xvar if not
                provided. Default : None
    data      : Optional. If provided, treats xvar and 
                yvar as keys of `data`, where `data` can
                be any key-accessed object, such as a dictionary
                or a pandas DataFrame. Default : None
           
    Returns:
    ---------
    x    : np.array. x bins
    y    : np.array. summary statistic being ploted
    ax   : matplotlib axes object
    """

    if not (data is None):
        xvar = data[xvar]
        yvar = data[yvar]
    
    if ax is None:
        fig, ax = plt.subplots()
        fig.set_size_inches(6,6)
    
    if categories is None:
        categories = np.unique(xvar)
    
    y = np.zeros(len(categories))
    
    for i,x in enumerate(categories):
        select = xvar == x    
        y[i] = rfunction( yvar[select] )
        
    
    ax.bar(categories, y)

    if len(categories) > 2: # personal preference
        ax.tick_params(axis='x', labelrotation=60)

    return bins, y, ax

def plot_continuous(xvar, 
                    yvar, 
                    rfunction,
                    data=None,
                    bins=10, 
                    ax = None):
    """
    Plot some reduction function of yvar in bins
    of xvar. This can be used, for example, to compute
    the running mean by passing 'np.mean' as `rfunction`,
    or more complex things like computing the fraction
    of points in each bin with some condition on yvar:
    
    Example, fraction of each points with associated y's
    > 10 could be done with passing:
    
        rfunction = lambda u : np.sum(u>10) / len(u)
    
    Parameters:
    ------------
    
    xvar      : np.array of x values OR valid key
                in data.
    yvar      : np.array of y values OR valid key
                in data.
    rfunction : a function that accepts an array
                and returns a single value. 
    data      : Optional. If provided, treats xvar and 
                yvar as keys of `data`, where `data` can
                be any key-accessed object, such as a dictionary
                or a pandas DataFrame. Default : None
    bins      : int or np.array. Number of bins or array
                representing the bins. If number of bins provided,
                chooses min and max of xvar as bounds. Default : 10

    Returns:
    ---------
    x    : np.array. x bins
    y    : np.array. summary statistic being ploted
    ax   : matplotlib axes object
    """

    if not (data is None):
        xvar = data[xvar]
        yvar = data[yvar]

    if isinstance(bins,int):
        bins = np.linspace( np.min(xvar), np.max(xvar), bins)

    if ax is None:
        fig, ax = plt.subplots()
        fig.set_size_inches(6,6)

    y = np.zeros(len(bins)-1)
    for i in np.arange(1,len(bins)):
        y[i-1] = rfunction( yvar[(xvar < bins[i]) & (xvar >= bins[i-1])] )

    ax.plot(0.5*(bins[1:]+bins[:-1]), y, lw = 3, color = 'black')

    return bins, y, ax




