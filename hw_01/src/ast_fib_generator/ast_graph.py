import ast

import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


class AstGraph:
    __labels = {}
    __colors = []
    __graph = nx.Graph()

    __basic_color = 'lightgreen'
    __list_color = 'pink'
    __ctx_color = 'lightgrey'
    __id_color = 'lightblue'
    __constant_color = 'violet'

    def __choose_color(self, node, field=None):
        if field == "ctx":
            color = self.__ctx_color
        elif field == 'id':
            color = self.__id_color
        elif node.__class__.__name__ == 'Constant':
            color = self.__constant_color
        else:
            color = self.__basic_color
        self.__colors.append(color)

    def __get_ast_label(self, node, field_name=None):
        if field_name is not None:
            res = field_name + "="
        else:
            res = ""
        res += node.__class__.__name__
        if node.__class__.__name__ == 'Constant':
            res += '\n"' + ast.unparse(node) + '"'
        return res

    def __visit(self, node, node_id):
        for field_name, value in ast.iter_fields(node):
            if isinstance(value, str):
                child_node_id = self.__graph.number_of_nodes()
                self.__graph.add_node(child_node_id)
                self.__choose_color(value, field_name)
                self.__graph.add_edge(node_id, child_node_id)
                self.__labels[child_node_id] = field_name + '\n"' + value + '"'
            elif isinstance(value, list):
                if len(value) == 0:
                    continue
                child_node_id = self.__graph.number_of_nodes()
                self.__graph.add_node(child_node_id)
                self.__colors.append(self.__list_color)
                self.__graph.add_edge(node_id, child_node_id)
                self.__labels[child_node_id] = field_name + '[]'
                for i in value:
                    subchild_node_id = self.__graph.number_of_nodes()
                    self.__graph.add_node(subchild_node_id)
                    self.__choose_color(i)
                    self.__graph.add_edge(child_node_id, subchild_node_id)
                    self.__labels[subchild_node_id] = self.__get_ast_label(i)
                    self.__visit(i, subchild_node_id)
            elif isinstance(value, ast.AST):
                child_node_id = self.__graph.number_of_nodes()
                self.__graph.add_node(child_node_id)
                self.__choose_color(value, field_name)
                self.__graph.add_edge(node_id, child_node_id)
                self.__labels[child_node_id] = self.__get_ast_label(value, field_name)
                self.__visit(value, child_node_id)

    def __get_node_size(self, label: str) -> int:
        a = max([len(line) for line in label.splitlines()])
        return a * a * 30 + 400

    def build(self, ast_obj):
        self.__labels[0] = self.__get_ast_label(ast_obj)
        self.__graph.add_node(0)
        self.__choose_color(ast_obj)
        self.__visit(ast_obj, 0)

    def draw(self, figsize):
        plt.figure(1, figsize)
        pos = graphviz_layout(self.__graph, prog="dot")
        nx.draw(self.__graph,
                pos,
                with_labels=True,
                node_shape='s',
                labels=self.__labels,
                font_size=8,
                node_size=[self.__get_node_size(self.__labels[i]) for i in range(self.__graph.number_of_nodes())],
                node_color=self.__colors
                )

        custom_lines = [Line2D([0], [0], color=self.__basic_color, lw=20),
                        Line2D([0], [0], color=self.__list_color, lw=20),
                        Line2D([0], [0], color=self.__ctx_color, lw=20),
                        Line2D([0], [0], color=self.__id_color, lw=20),
                        Line2D([0], [0], color=self.__constant_color, lw=20)]
        plt.legend(custom_lines, ['basic color', 'list', 'ctx', 'id', 'constant'], fontsize=50)
