import os

import numpy as np

from hw_03.src.matrix_my import MatrixMy
from hw_03.src.matrix_numpy import MatrixNumpy


def generate_easy(folder_path):
    np.random.seed(0)
    a = MatrixMy(np.random.randint(0, 10, (10, 10)))
    b = MatrixMy(np.random.randint(0, 10, (10, 10)))
    with open(folder_path + "matrix+.txt", "w") as file:
        file.write((a + b).__str__())
    with open(folder_path + "matrix*.txt", "w") as file:
        file.write((a * b).__str__())
    with open(folder_path + "matrix@.txt", "w") as file:
        file.write((a @ b).__str__())


def generate_medium(folder_path):
    np.random.seed(0)
    a = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
    b = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
    with open(folder_path + "matrix+.txt", "w") as file:
        file.write((a + b).__str__())
    with open(folder_path + "matrix*.txt", "w") as file:
        file.write((a * b).__str__())
    with open(folder_path + "matrix@.txt", "w") as file:
        file.write((a @ b).__str__())


def generate_hard(folder_path):
    a = MatrixMy([[6, 8], [0, 0]])
    b = MatrixMy([[1, 0], [0, 1]])
    c = MatrixMy([[10, 0], [0, 0]])
    d = MatrixMy([[1, 0], [0, 1]])
    a.to_file(folder_path + "A.txt")
    b.to_file(folder_path + "B.txt")
    c.to_file(folder_path + "C.txt")
    d.to_file(folder_path + "D.txt")

    ab = a @ b
    c._matmul_cache = {}
    cd = c @ d

    ab.to_file(folder_path + "AB.txt")
    cd.to_file(folder_path + "CD.txt")

    with open(folder_path + "hash.txt", "w") as file:
        file.write("A hash: ")
        file.write(a.__hash__().__str__() + "\n")
        file.write("C hash: ")
        file.write(c.__hash__().__str__() + "\n")


def main():
    artifacts_paths = ["artifacts/easy/", "artifacts/medium/", "artifacts/hard/"]
    for path in artifacts_paths:
        if not os.path.exists(path):
            os.makedirs(path)
    generate_easy(artifacts_paths[0])
    generate_medium(artifacts_paths[1])
    generate_hard(artifacts_paths[2])


if __name__ == '__main__':
    main()
