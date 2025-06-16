from scipy.stats import norm, lognorm, expon, triang, uniform
import numpy as np


def param_stoiip(
    df,
    row,
    dist_col,
    loc_col,
    scale_col,
    reali,
    sc_col=None,
    lim_min_col=None,
    lim_max_col=None,
    seed=None,
):
    """
    This function has the following goal. To return numpy arrays of any Stoiip variable
     like area, h, porosity, swi, boi. Furthermore, this numpy array contains random
     values from various continuous distributions.

    Parameters
    ----------
    df
        Pandas DataFrame
    row
        Row index
    dist_col
        Distribution column (Normal, Log-Normal, Exponential, Triangular, Uniform)
    loc_col
        Loc column
    scale_col
        Scale column
    reali
        Number o realizations or generations
    sc_col
        S or C column
    lim_min_col
        Minimum limit column
    lim_max_col
        Maximum limit column
    seed
        Number of seed

    Returns
    -------
    A Numpy array with random values generated for any POES parameter (Area, h, swi,
     etc)
    """

    if seed is None:
        rng = np.random.default_rng()
    else:
        rng = np.random.default_rng(seed)

    if df.loc[row, dist_col] == "Log-Normal" or df.loc[row, dist_col] == "Triangular":
        if df.loc[row, dist_col] == "Log-Normal":
            param = lognorm.rvs(
                s=df.loc[row, sc_col],
                loc=df.loc[row, loc_col],
                scale=df.loc[row, scale_col],
                size=reali,
                random_state=rng,
            )

            param = np.where(
                param < df.loc[row, lim_min_col], df.loc[row, lim_min_col], param
            )

            param = np.where(
                param > df.loc[row, lim_max_col], df.loc[row, lim_max_col], param
            )

        elif df.loc[row, dist_col] == "Triangular":
            param = triang.rvs(
                c=df.loc[row, sc_col],
                loc=df.loc[row, loc_col],
                scale=df.loc[row, scale_col],
                size=reali,
                random_state=rng,
            )

    elif df.loc[row, dist_col] == "Normal":
        param = norm.rvs(
            loc=df.loc[row, loc_col],
            scale=df.loc[row, scale_col],
            size=reali,
            random_state=rng,
        )

        param = np.where(
            param < df.loc[row, lim_min_col], df.loc[row, lim_min_col], param
        )

        param = np.where(
            param > df.loc[row, lim_max_col], df.loc[row, lim_max_col], param
        )

    elif df.loc[row, dist_col] == "Exponential":
        param = expon.rvs(
            loc=df.loc[row, loc_col],
            scale=df.loc[row, scale_col],
            size=reali,
            random_state=rng,
        )

        param = np.where(
            param > df.loc[row, lim_max_col], df.loc[row, lim_max_col], param
        )

    elif df.loc[row, dist_col] == "Uniform":
        param = uniform.rvs(
            loc=df.loc[row, loc_col],
            scale=df.loc[row, scale_col],
            size=reali,
            random_state=rng,
        )

    return param
