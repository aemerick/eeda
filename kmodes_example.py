from kneed import KneeLocator
from kmodes.kmodes import KModes



def fit_clusters(df,
                 n_min_clusters = 1,
                 n_max_clusters = 15
                 to_encode = None):
    """
    Assumes user
    If to_encode is None, assumes things are already label encoded. Otherwise
    performs label encoding on each categorical in `to_encode`
    """

    #
    # label encode
    #
    le = {}
    if (to_encode is None):
        df_enc = df.copy(deep=True)
    else:
        df_enc = df.copy(deep=True)
        for fname in to_encode:
            le[fname]     = preprocessing.LabelEncoder()
            df_enc[fname] = le[fname].fit_transform(df_enc[fname])

    # iterate over KModes a few times
    n_iter = n_max_clusters - n_min_clusters + 1
    cost = np.zeros(n_iter)
    for i in range(n_iter):
        km = KModes(n_clusters= (i+1), n_init = 1, verbose=0)
        km.fit(df_enc)
        cost[i] = km.cost_

    # locate the elbow
    kl = KneeLocator(range(n_iter), cost, curve="convex", direction="decreasing")
    n_clusters = kl.elbow

    # generate the final kmodes fit
    km = KModes(n_clusters=n_clusters, n_init = 1, verbose=0)
    clusters = km.fit_predict(df_enc)

    if not (to_encode is None):
        df_renc = df_enc.copy()
        for fname in to_encode:
            df_renc[fname] = le[fname].inverse_transform(df_renc[fname])
        df_ind_res = df_renc.reset_index()
    else:
        df_ind_res = df_enc.reset_index()

    clustersDF = pd.DataFrame(clusters)
    clustersDF.columns = ['cluster_predicted']
    clustersDF = pd.concat([clustersDF, df_ind_res], axis=1).reset_index()
    clustersDF
