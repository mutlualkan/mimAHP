from .pairwise import comparisiondataframe, normalizedataframe
from .weights import calculate_weights
from .consistency import consistency_ratio

def mimahp(criterialist):
    comparisions, comparisionmatrix = comparisiondataframe(criterialist=criterialist)
    normalization = normalizedataframe(comparisions)
    weights = calculate_weights(normalization)
    cr = consistency_ratio(comparisionmatrix, weights)
    return [comparisions, normalization, weights, cr]