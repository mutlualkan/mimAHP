import numpy as np


def consistency_ratio(matrix, weights):
    n = matrix.shape[0]
    lambda_max = np.sum(np.dot(matrix, weights) / weights) / n
    ci = (lambda_max - n) / (n - 1)

    # RI: Random Consistency Index (for 3–15 criteria)
    RI = [0.00, 0.00, 0.58, 0.90, 1.12,
          1.24, 1.32, 1.41, 1.45, 1.49,
          1.51, 1.53, 1.56, 1.57, 1.59]

    ri = RI[n - 1] if n <= 10 else 1.49  # Approximately for more than 15
    cr = ci / ri if ri else 0
    return cr
