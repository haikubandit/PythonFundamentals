def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
        >>> m3 = [
        ...    [16, 2, 9],
        ...    [4, 5, 6],
        ...    [2, 8, 5],
        ... ]
        >>> sum_up_diagonals(m3)
        42
    """
    size = len(matrix)
    TL_to_BR = sum(matrix[n][n] for n in range(size))
    TR_to_BL = sum(matrix[n][size - n - 1] for n in range(size))

    return TL_to_BR + BL_to_TR

    # course solution

    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total

    # or, probably too tersely:
    #
    # return sum([matrix[i][i] + matrix[i][-1 - i] for i in range(len(matrix))])