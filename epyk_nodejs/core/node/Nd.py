
from epyk_nodejs.core.node import NdHttp
from epyk_nodejs.core.node import NdCrypto
from epyk_nodejs.core.node import NdAssert
from epyk_nodejs.core.node import NdFs
from epyk_nodejs.core.node import NdInspector
from epyk_nodejs.core.node import NdHttp2

from epyk_nodejs.core.node import NdGlobal


class Modules(NdGlobal.NdGlobal):

  def __init__(self, src):
    self._report = src

  @property
  def http(self):
    """

    https://nodejs.org/docs/latest-v13.x/api/http.html
    """
    return NdHttp.Http(self._report)

  @property
  def crypto(self):
    """

    https://nodejs.org/docs/latest-v13.x/api/http.html
    """
    return NdCrypto.Cipher(self._report)

  @property
  def assert_testing(self):
    """

    https://nodejs.org/docs/latest-v13.x/api/http.html
    """
    return NdAssert.Assert(self._report)

  @property
  def fs(self):
    """

    https://nodejs.org/docs/latest-v13.x/api/http.html
    """
    return NdFs.Fs(self._report)

  @property
  def http2(self):
    """

    https://nodejs.org/docs/latest-v13.x/api/http.html
    """
    return NdHttp2.Http2(self._report)

  @property
  def inspector(self):
    """

    https://nodejs.org/docs/latest-v13.x/api/http.html
    """
    return NdInspector.Inspector(self._report)
