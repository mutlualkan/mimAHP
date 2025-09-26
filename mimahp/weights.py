import math

def calculate_weights(normalizeddataframe):
    """

    :param normalizeddataframe: This is the dataframe obtained by normalizing the matrix obtained from the pairwise
    comparison matrix.
    :return: This is a single-column dataframe consisting of the arithmetic averages of the rows of the dataframe
    containing the normalization result. This dataframe contains the decision weights of the criteria.
    """
    sizeof_normdf = normalizeddataframe.size
    root = math.isqrt(sizeof_normdf)
    if root * root == sizeof_normdf:
        weightdf = normalizeddataframe.select_dtypes(include = 'number')
        weightdf = weightdf.mean(axis=1)

    return weightdf
