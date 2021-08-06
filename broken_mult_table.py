import sys


def mult_table(a, b):
    """ Create a multiplication table

    Args:
       a (int)
       b (int)

    Expected result for a = 3, b = 5:

    => [[1, 2, 3,  4,  5],
        [2, 4, 6,  8, 10],
        [3, 6, 9, 12, 15],]

    """
    table = [[]] * a
    for i in range(1, n+1):
        for j in range(1, m+1):
            table[i-1].append(i * j)

    return table


def print_table(table):
    """Print every row in mult. table"""
    for row in table:
        print(row)


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    table = mult_table(n, m)
    print_table(table)
