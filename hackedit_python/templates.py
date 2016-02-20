"""
This module contains the COBOL templates provider plugin.
"""
from hackedit import api


class PyTemplatesProvider(api.plugins.TemplateProviderPlugin):
    @staticmethod
    def get_label():
        return 'Python'

    @staticmethod
    def get_url():
        return 'https://github.com/HackEdit/python_templates.git'
