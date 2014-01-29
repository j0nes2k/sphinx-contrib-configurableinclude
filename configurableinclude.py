from docutils.parsers.rst.directives.misc import Include
from docutils import nodes

def setup(app):
    app.add_config_value('configurableinclude_paths', {}, False)
    app.add_directive('include_from_config', ConfigurableInclude)



class ConfigurableInclude(Include):
    """ Include content from a separate source file, configurable paths.

    This allows adding setting base paths in ``conf.py`` and including relative
    to these paths in the rST files.

    Usage:
       - in conf.py: configurableinclude_paths = { 'module1': '/var/repositories/module1' }
       - in rST file: .. include_from_config:: module1 /docs/databaseaccess.rst
    """

    required_arguments = 2

    def __init__(self, name, arguments, *args):
        super(ConfigurableInclude, self).__init__(name, arguments, *args)

        paths = self.state.document.settings.env.config.configurableinclude_paths

        if self.arguments[0] in paths:
            self.arguments[0] = paths[self.arguments[0]] + self.arguments[1]
        else:
            raise self.error("Configuration module %s not found" % self.arguments[0])
