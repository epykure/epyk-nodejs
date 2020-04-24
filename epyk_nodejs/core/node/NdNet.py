
from epyk_nodejs.core.node import NdGlobal


class Server(NdGlobal.NdGlobal):

  def __init__(self, src, options, connectionListener):
    """

    :param src:
    :param options:
    :param connectionListener:
    """

  def address(self):
    pass

  def close(self, callback):
    """

    :param callback:
    """

  def getConnections(self, callback):
    """

    :param callback:
    """

  def listen(self):
    """

    """

  def ref(self):
    """

    """

  def unref(self):
    """

    """


class Socket(NdGlobal.NdGlobal):

  def connect(self, options=None, connectListener=None):
    """

    """

  def destroy(self, exception=None):
    """

    :param exception:
    """

  def pause(self):
    """

    """

  def ref(self):
    """

    """

  def unref(self):
    """

    """

  def resume(self):
    """

    :return:
    """

  def setEncoding(self, encoding=None):
    """

    :param encoding:
    """
    pass

  def setTimeout(self, timeout, callback):
    """

    :param timeout:
    :param callback:
    """

  def write(self, data, encoding, callback):
    """

    :param data:
    :param encoding:
    :param callback:
    """