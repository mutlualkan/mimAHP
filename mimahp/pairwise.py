import itertools
import numpy as np
import pandas as pd

def comparisonmatrix(criterialist):
    """
    :param criterialist: List object of criteria
    :return: Dictionary variable ( key: Tuple variable, value : float variable)
    """
    if len(criterialist)>=3:
        pairs = list(itertools.combinations(criterialist, 2))
        relations = {}
        for a, b in pairs:
            while True:
                try:
                    value = float(input(f"{a} vs {b} :"))
                    if value > 0 and value <= 9.0:
                        relations[(a, b)] = round(value, 8)
                        relations[(b, a)] = round(1 / value, 8)
                        print(f"/////{b} vs {a} :", relations[(b, a)])
                        break
                    else:
                        print("Please enter the appropriate value for Saaty's pairwise comparison scale.")
                except ValueError:
                    break
        # for pair, relation in relations.items():
        #     print(f"{pair[0]} vs {pair[1]}: {relation}")
        # print(relations)
        return relations
    else:
        return {}

def comparisiondataframe(criterialist):
    """

    :param criterialist : List object of criteria
    :return: Comparision values datfarme
    """
    df=''
    if len(criterialist)>2:
        comparisiondict = comparisonmatrix(criterialist)

        unitmatrixsize = len(criterialist)
        unitmatrix = np.identity(unitmatrixsize)
        df = pd.DataFrame(unitmatrix, index = criterialist, columns = criterialist)
        for (col, idx), value in comparisiondict.items():
            if col in df.columns and idx in df.index:
                df.at[col, idx] = value
            else:
                print(f"Warning: {col} column or {idx} index not find.")
    return df, df.to_numpy()


def normalizedataframe(comparisiondataframe):
    """

    :param comparisiondataframe:Dataframe containing the results of pairwise comparisons of criteria.
    :return: Normalization is achieved by dividing the numerical values in the comparison dataframe by the total of the
    corresponding column. In the new dataframe created as a result of this normalization, the sum of each column
    containing a numerical value is checked to ensure it equals 1. If the column totals equal 1, the normalization
    is successful. The new dataframe resulting from normalization is returned as the function result.
    """

    numeric_cols = comparisiondataframe.select_dtypes(include='number').columns
    col_sums = comparisiondataframe[numeric_cols].sum()

    #Prevention against division-by-zero errors: Columns with a total of 0 remain constant.
    col_sums = col_sums.replace(0,1)

    normalized_df = comparisiondataframe.copy()
    normalized_df[numeric_cols] = normalized_df[numeric_cols] / col_sums

    return normalized_df
