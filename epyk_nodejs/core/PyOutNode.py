
import os
from epyk.core.py import PyOuts


class PyOuts(PyOuts.PyOuts):

  def node_files(self, path):
    """

    :param path:
    """
    for folder in ["stylesheets", 'modules', 'components', 'pages']:
      sub_path = os.path.join(path, folder)
      if not os.path.exists(sub_path):
        os.makedirs(sub_path, exist_ok=True)
    htmlParts, cssParts = ["<link rel='stylesheet' href='/stylesheets/%s.css' />" % self._options['module']], dict(self._report.body.style.get_classes_css())
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
        #f.write("%s %s\n" % (c, d))

    # Then write the app itself
    with open(os.path.join(path, "pages", "%s.html" % self._options['module']), "w") as f:
      f.write("\n".join(htmlParts))

    #body = str(self._report.body.set_content(self._report, "\n".join(htmlParts)))
    #esults = self._to_html_obj(htmlParts, cssParts)
    #print(results)