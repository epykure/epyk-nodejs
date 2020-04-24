
import os
import sys

from epyk.core import Page
from epyk_nodejs.core import PyOutNode
from epyk_nodejs.core.node import NdGlobal


class Report(Page.Report):

  def __init__(self):
    super(Report, self).__init__()
    self._node = None
    # Override the icon to use the one from the github repository
    # self.headers._favicon_url = "https://raw.githubusercontent.com/epykure/epyk-materials/master/epyk_materials/static/images/epyk_materials_logo.ico"

  @property
  def node(self):
    """
    https://nodejs.org/docs/latest-v13.x/api/globals.html

    """
    if self._node is None:
      self._node = NdGlobal.NdGlobal(self)
    return self._node

  @property
  def outs(self):
    """

    """
    module = os.path.split(sys._getframe().f_back.f_code.co_filename)[1][:-3]
    return PyOutNode.PyOuts(self, options={"module": module})
