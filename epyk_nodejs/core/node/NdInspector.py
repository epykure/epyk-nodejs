
from epyk_nodejs.core.node import NdGlobal


class Inspector(NdGlobal.NdGlobal):

  def close(self):
    pass

  def console(self):
    pass

  def open(self):
    pass

  def url(self):
    pass

  def waitForDebugger(self):
    pass


class Session(NdGlobal.NdGlobal):

  def connect(self):
    pass

  def connectToMainThread(self):
    pass

  def disconnect(self):
    pass

  def post(self, post, method, paramsq, callback):
    """

    :param post:
    :param method:
    :param paramsq:
    :param callback:
    """