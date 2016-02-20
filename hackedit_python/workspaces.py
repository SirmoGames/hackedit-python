try:
    from IPython.qt.console import rich_ipython_widget
except ImportError:
    rich_ipython_widget = None
    ipython_available = False
else:
    ipython_available = True


class PythonWorkspace:
    def get_data(self):
        data = {
          'name': 'Python',
          'description': 'Default pure python workspace.',
          'plugins': [
            'FindReplace',
            'DocumentOutline',
            'OpenDocuments',
            'Terminal',
            'HtmlPreview',
            'PyRefactor',
            'PyRun',
            'PyContextMenus',
            'PyOpenModule',
            'PyCodeEditorIntegration',
            'CleanPycFiles'
            ]
        }
        if ipython_available:
            data['plugins'].append('IPythonConsole')
        return data
