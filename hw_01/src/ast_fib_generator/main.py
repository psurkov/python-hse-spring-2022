import ast

import matplotlib.pyplot as plt

from ast_fib_generator.ast_graph import AstGraph


def main():
    with open("fibonacci.py") as f:
        fibonacci_func_text = f.read()

    ast_object = ast.parse(fibonacci_func_text)

    graph = AstGraph()
    graph.build(ast_object)
    graph.draw((25, 20))
    plt.savefig("artifacts/ast.png")


if __name__ == '__main__':
    main()
