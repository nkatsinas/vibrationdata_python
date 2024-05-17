# Vibrationdata for Python
This package was copied from the [Vibrationdata Wordpress](https://vibrationdata.wordpress.com/2014/04/02/python-signal-analysis-package-gui/) site and converted to a Python package.

Email: tom@vibrationdata.com / nick@nickkatsinas.com

## Installing the Package from Source
In the future, this $should$ be installed by command line from PyPI, but for now, clone the package locally (or download) and navigate to the directory containing the `pyproject.toml` file and run the following command to install:
```console
pip install .
```
## Using the GUI
Once the package is installed, the GUI package can be started from running the following command in a console:
```console
python -m vibrationdata.vibrationdata
```
...
or the following commands from a python REPL session:
```python
from vibrationdata import vibrationdata
```