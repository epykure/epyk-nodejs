
from epyk_nodejs.core.node import NdGlobal


class Certificate(NdGlobal.NdGlobal):

  def exportChallenge(self, spkac):
    pass

  def exportPublicKey(self, spkac, encoding):
    """

    :param spkac:
    :param encoding:
    """


class Cipher(NdGlobal.NdGlobal):
  def final(self, outputEncoding):
    pass

  def setAAD(self, buffer, options):
    pass

  def getAuthTag(self):
    pass

  def setAutoPadding(self, autoPadding=True):
    pass


class Decipher(NdGlobal.NdGlobal):
  def final(self, outputEncoding):
    pass

  def setAAD(self, buffer, options):
    pass

  def setAuthTag(self, buffer):
    pass
