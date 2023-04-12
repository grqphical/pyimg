# Plugin API Based on: https://gist.github.com/dorneanu/cce1cd6711969d581873a88e0257e312
import os
from importlib import util

class BasePlugin:
    """Base class that all plugins extend from"""

    plugins = []

    # For every class that inherits from the current,
    # the class name will be added to plugins
    def __init_subclass__(self, **kwargs):
        super().__init_subclass__(**kwargs)
        self.plugins.append(self)

# Small utility to automatically load modules
def load_module(path):
    name = os.path.split(path)[-1]
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Get current path
path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)

for fname in os.listdir(dirpath):
    # Load only "real modules"
    if not fname.startswith('.') and \
       not fname.startswith('__') and fname.endswith('.py'):
        try:
            load_module(os.path.join(dirpath, fname))
        except Exception:
            print(Exception)