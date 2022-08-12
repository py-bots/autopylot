from webbrowser import Chrome
from my_autopylot.CheckSystem import python_version, python_37, python_38, python_39, python_310
from importlib import import_module
import sys

MODULE_NAME = 'my_autopylot.Windows.functions.chrome.chrome' + \
    str(sys.version_info.major) + str(sys.version_info.minor)

if python_version in [python_37, python_38, python_39, python_310]:
    Chrome = import_module(MODULE_NAME)
else:
    print("Python Version Not Supported")
    sys.exit()
