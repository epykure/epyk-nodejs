
import os
import logging

from epyk.core.js import Imports


class NodeImportManager(Imports.ImportManager):

  def to_node(self, modules, excluded_packages=None, ext_config=None, node_modules_path=None):
    """
    Description:
    ------------
    Transform

    Attributes:
    ----------
    :param data: Dictionary. The Report modules to resolve
    :param excluded_packages: Optional. List. The packages to exclude
    :param ext_config: Optional. Dictionary. The external configurations
    """
    deps_level, alias_to_name = {}, {}
    for m in modules:
      if excluded_packages is not None and m in excluded_packages:
        continue

      if 'register' in Imports.JS_IMPORTS[m]:
        if 'req' in Imports.JS_IMPORTS[m]:
          max_level = max([deps_level[alias['alias']] if alias['alias'] in deps_level else -1 for alias in Imports.JS_IMPORTS[m]['req']])
          deps_level[m] = max_level + 1
        else:
          deps_level[m] = 0

    requirements = []
    for k, v in sorted(deps_level.items(), key=lambda item: item[1]):
      mod_register = Imports.JS_IMPORTS[k]['register']
      if not 'npm' in mod_register:
        if ext_config is not None and k in ext_config:
          requirements.append("var %s = require('%s')" % (mod_register.get('name', k), ext_config['npm']))
        else:
          raise Exception("No valid package definition for %s in Imports" % k)

      else:
        module_path = os.path.join(node_modules_path, mod_register['npm'].split("/")[0])
        if not os.path.exists(module_path):
          logging.warning("Module %s not loaded on the NodeJs server, please check the npm packages" % k)

        requirements.append("var %s = require('%s')" % (mod_register.get('name', mod_register.get('alias')), mod_register['npm']))
    return requirements
