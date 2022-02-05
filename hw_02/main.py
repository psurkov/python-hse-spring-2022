import os
import functools

from ast_fib_generator import main


def generate_latex_table(data: list[list[str]]) -> str:
    return "\\begin{tabular}{||" + functools.reduce(lambda l, _: l + "c|", data[0], "") + "|}\n\\hline\n" + \
           functools.reduce(
               lambda l, r: l + "\n\\hline\n" + r,
               map(
                   lambda line: functools.reduce(lambda l, r: l + " & " + r, line) + " \\\\",
                   data
               )
           ) + \
           "\n\\hline\n\\end{tabular}\\\\\n"


def generate_latex_header(title: str, author: str, date: str) -> str:
    return (
        "\\documentclass{article}\n"
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage{graphicx}\n"
        f"\\title{{{title}}}\n"
        f"\\author{{{author}}}\n"
        f"\\date{{{date}}}\n"
        "\\begin{document}\n"
        "\\maketitle\n\n"
    )


def generate_latex_footer() -> str:
    return "\\end{document}"


def insert_image(img_path, scale) -> str:
    return f"\\includegraphics[scale={scale}]{{{img_path}}}\n"


if __name__ == '__main__':
    if not os.path.exists("artifacts"):
        os.mkdir("artifacts")
    with open('artifacts/file.tex', 'w') as f:
        f.write(generate_latex_header("Hello from Python!", "Petya Surkov", "5 February"))
        f.write(generate_latex_table(
            [["title1", "title2", "title3"],
             ["text1", "text2", "text3"],
             ["text4", "text5", "text6"]]
        ))
        main.main()
        f.write(insert_image("ast.png", 0.22))
        f.write(generate_latex_footer())
