"""
This module contains the COBOL templates provider plugin.
"""
from hackedit import api


class PyTemplatesProvider(api.plugins.TemplateProviderPlugin):
    def get_label(self):
        return 'Python'

    def get_url(self):
        return 'https://github.com/HackEdit/python_templates.git'
