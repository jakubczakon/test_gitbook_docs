import neptune
import os.path

lib_path = os.path.dirname(os.path.dirname(neptune.__file__))
print(lib_path)