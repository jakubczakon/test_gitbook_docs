import neptunecontrib
import os.path

lib_path = os.path.dirname(os.path.dirname(neptunecontrib.__file__))
print(lib_path)