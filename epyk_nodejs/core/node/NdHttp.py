
from epyk_nodejs.core.node import NdGlobal


class Http(NdGlobal.NdGlobal):

  def createServer(self, options, requestListener=None):
    pass

  def createConnection(self, options, callback=None):
    pass

  def get(self, url, options, callback):
    """

    :param url:
    :param options:
    :param callback:
    """

  def request(self, url, options, callback):
    """

    :param url:
    :param options:
    :param callback:
    """


class ServerResponse(NdGlobal.NdGlobal):

  def cork(self):
    pass

  def end(self):
    pass

  def flushHeaders(self):
    pass

  def getHeader(self):
    pass

  def getHeaderNames(self):
    pass

  def getHeaders(self):
    pass

  def hasHeader(self, name):
    """

    :param name:
    """
    pass

  def removeHeader(self, name):
    """

    :param name:
    """

  def setHeader(self, name, value):
    """

    :param name:
    :param value:
    """

  def setTimeout(self, msecs, callback):
    """

    :param msecs:
    :param callback:
    """
    pass

  def uncork(self):
    pass

  def write(self, chunk, encoding=None, callback=None):
    """

    :param chunk:
    :param encoding:
    :param callback:
    """

  def writeContinue(self):
    """

    :return:
    """

  def writeHead(self, statusCode, statusMessage, headers):
    """

    :param statusCode:
    :param statusMessage:
    :param headers:
    """

  def writeProcessing(self):
    """
    Sends a HTTP/1.1 102 Processing message to the client, indicating that the request body should be sent.
    """
