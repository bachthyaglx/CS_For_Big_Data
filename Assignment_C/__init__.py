import os
"""
Special file __init__.py marks a directory as a Python package.
A Python Package is a collection of Python modules with an
__init__.py File. The file is executed once when any .py file
from the directory is imported for the first time.
"""


def package_dir(file):
    """
    Return name of directory of this package.
    """
    path = os.path.normpath(file).split(os.sep)
    return path[len(path)-2]    # e.g. "C_expressions"


def project_path(file):
    """
    Return path to project directory.
    """
    path = os.path.normpath(file).split(os.sep)
    return os.path.dirname(file)[:-len(PACKAGE_DIR)-1]


def import_sol_module(file):
    """
    Import and return module with name "file + '_sol'".
    Raises ImportError exception, if _sol file does not exist.
    """
    sol_module = (file.split("\\")[-1:])[0].split(".")[0] + "_sol"
    return __import__(sol_module, globals(), locals(), [], 0)


# name of this package directory
PACKAGE_DIR = package_dir(__file__)

# path to project directory, in which this module resides 
PROJECT_PATH = project_path(__file__)
