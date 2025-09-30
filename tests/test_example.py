from mimahp.mimahp import mimahp

criterias=['A', 'B', 'C', 'D', 'E', 'F']

c, n, w, cr = mimahp(criterialist=criterias)
print('Comparison Matrix : \n ', c)
print('Normalization Matrix : \n  ', n)
print('Criteria Decision Weights : \n', w)
print('Consistency Ratio : \n', round(cr,8))