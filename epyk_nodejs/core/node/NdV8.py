
from epyk_nodejs.core.node import NdGlobal


class V8(NdGlobal.NdGlobal):


  def cachedDataVersionTag(self):
    pass

  def getHeapSpaceStatistics(self):
    pass

  def getHeapSnapshot(self):
    pass

  def getHeapStatistics(self):
    pass

  def getHeapCodeStatistics(self):
    pass

  def setFlagsFromString(self, flags):
    pass

  def writeHeapSnapshot(self, filane):
    pass

  def serialize(self, value):
    pass

  def deserialize(self, buffer):
    pass


class Serializer(NdGlobal.NdGlobal):

  def writeHeader(self):
    """

    :return:
    """

  def writeValue(self, value):
    """

    :param value:
    :return:
    """

  def releaseBuffer(self):
    """

    :return:
    """

  def transferArrayBuffer(self, id, arrayBuffer):
    """

    :param id:
    :param arrayBuffer:
    """

  def writeUint32(self, value):
    """

    :param value:
    """

  def writeUint64(self, hi, lo):
    """

    :return:
    """

  def writeDouble(self, value):
    """

    :param value:
    """

  def writeRawBytes(self, buffer):
    """
    
    :param buffer:
    :return:
    """