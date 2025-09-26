from .pairwise import comparisiondataframe, normalizedataframe
from .weights import calculate_weights
from .consistency import consistency_ratio

# def ahp(criteria_count, comparisons, criterialist):
def mimahp(criterialist):
    # comparisions=comparisonmatrix(criterialist)
    comparisions, comparisionmatrix = comparisiondataframe(criterialist=criterialist)
    normalization = normalizedataframe(comparisions)
    weights = calculate_weights(normalization)
    cr = consistency_ratio(comparisionmatrix, weights)
    # return weights, cr
    # return comparisions
    return [comparisions, normalization, weights, cr]