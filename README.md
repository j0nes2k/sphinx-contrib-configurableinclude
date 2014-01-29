sphinx-contrib-configurableinclude
==================================

Sphinx directive to include content from a separate source file with configurable base paths. 

Usage:

       - in conf.py: configurableinclude_paths = { 'module1': '/var/repositories/module1' }
       - in rST file: .. include_from_config:: module1 /docs/databaseaccess.rst
