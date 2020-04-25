
import os

from epyk.core.py import PyOuts

from epyk_nodejs.core import Imports


class PyOuts(PyOuts.PyOuts):

  def node_files(self, path, node_modules_path=None):
    """

    :param path:
    """
    for folder in ["stylesheets", 'modules', 'components', 'pages']:
      sub_path = os.path.join(path, folder)
      if not os.path.exists(sub_path):
        os.makedirs(sub_path, exist_ok=True)
    htmlParts, cssParts = ["<head><link rel='stylesheet' href='/stylesheets/%s.css' /><style>%s</style></head>" % (self._options['module'], "\n".join(self._report._cssText))], dict(self._report.body.style.get_classes_css())
    for objId in self._report.content:
      if self._report.htmlItems[objId].inReport:
        htmlParts.append(self._report.htmlItems[objId].html())
        cssParts.update(self._report.htmlItems[objId].style.get_classes_css())

    # Create a style file for the report app
    with open(os.path.join(path, "stylesheets", "%s.css" % self._options['module']), "w") as f:
      for v in cssParts.values():
        f.write("%s\n" % v)

    # Create a dedicated builder module for the app
    # https://www.w3schools.com/nodejs/nodejs_modules.asp
    with open(os.path.join(path, "modules", "%s.js" % self._options['module']), "w") as f:
      for c, d in self._report._props.get('js', {}).get("constructors", {}).items():
        f.write("exports.%s = function(htmlObj%s" % (c,  d.split("function %s(htmlObj" % c)[-1]))

    # Then write the app itself
    # First check the various requirements to be added
    with open(os.path.join(path, "pages", "%s.html" % self._options['module']), "w") as f:
      f.write("<body>%s</body>"% "\n".join(htmlParts))

    node_modules_path = node_modules_path or os.path.join(path, 'node_modules')
    importMng = Imports.NodeImportManager(online=True, report=self._report)
    print(importMng.to_node((self._report.jsImports), node_modules_path=node_modules_path))
    #body = str(self._report.body.set_content(self._report, "\n".join(htmlParts)))
    #esults = self._to_html_obj(htmlParts, cssParts)
    #print(results)
