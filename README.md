sphinx-contrib-configurableinclude
==================================

Sphinx directive to include content from a separate source file with configurable base paths. 

Installation
------------

- add directory to extension search path in ``conf.py``: ``sys.path.append(os.path.abspath('exts'))``
- add the extension to ``extension``:``extensions = [ 'configurableinclude' ]``

Usage
-----

- in conf.py: ``configurableinclude_paths = { 'module1': '/var/repositories/module1' }``
- in rST file: ``.. include_from_config:: module1 /docs/databaseaccess.rst``
