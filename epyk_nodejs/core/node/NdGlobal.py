

class NdGlobal(object):

  def __init__(self, src):
    self._report = src

  def require(self):
    """
    Used to import modules, JSON, and local files. Modules can be imported from node_modules.
    Local modules and JSON files can be imported using a relative path (e.g. ./, ./foo, ./bar/baz, ../foo) that will be resolved against the directory named by __dirname (if defined) or the current working directory. The relative paths of POSIX style are resolved in an OS independent fashion, meaning that the examples above will work on Windows in the same way they would on Unix systems.

    https://nodejs.org/docs/latest-v13.x/api/modules.html#modules_exports
    """

  def exports(self):
    """
    A reference to the current module, see the section about the module object. In particular, module.exports is used for defining what a module exports and makes available through require().

    https://nodejs.org/docs/latest-v13.x/api/modules.html#modules_exports

    """

  def module(self):
    """
    A reference to the current module, see the section about the module object.
    In particular, module.exports is used for defining what a module exports and makes available through require().

    :return:
    """
