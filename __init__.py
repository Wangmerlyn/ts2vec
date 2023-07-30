import os, sys

print(os.path.dirname(os.path.realpath("ts2vec/__init__.py")))
sys.path.append(os.path.dirname(os.path.realpath("ts2vec/__init__.py")))
from .ts2vec import *
