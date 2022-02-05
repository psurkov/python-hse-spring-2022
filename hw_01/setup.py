import setuptools

install_requires = ["cycler==0.11.0",
                    "fonttools==4.29.0",
                    "graphviz==0.19.1",
                    "kiwisolver==1.3.2",
                    "matplotlib==3.5.1",
                    "networkx==2.6.3",
                    "numpy==1.22.1",
                    "packaging==21.3",
                    "Pillow==9.0.0",
                    "pydot==1.4.2",
                    "pygraphviz==1.8",
                    "pyparsing==3.0.7",
                    "python-dateutil==2.8.2",
                    "six==1.16.0"]

setuptools.setup(
    name="fib-ast-generator",
    version="1.5",
    author="Petr Surkov",
    install_requires=install_requires,
    url="https://github.com/psurkov/python-hse-spring-2022",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
