FROM python:3.9
COPY main.py main.py
COPY fibonacci.py fibonacci.py
RUN apt-get update; apt-get install -y texlive graphviz graphviz-dev python3-pygraphviz
RUN python3.9 -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple fib-ast-generator==1.5
RUN python3.9 main.py

WORKDIR artifacts
RUN pdflatex file.tex
RUN rm file.aux file.log