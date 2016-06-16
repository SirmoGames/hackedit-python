"""
This module contains a plugin that show a terminal in the bottom
area of the window.
"""
from PyQt5 import QtCore, QtGui, QtWidgets

from pyqode.core.api import ColorScheme
from pyqode.python.widgets import PyConsole as PyConsoleWidget

from hackedit import api
from hackedit.app import settings

from .interpreters import PythonManager


class PyConsole(api.plugins.WorkspacePlugin):
    """
    Adds a python console widget to the IDE.
    """
    def activate(self):
        self.widget = PyConsoleWidget(parent=api.window.get_main_window(), color_scheme=settings.color_scheme())
        dock = api.window.add_dock_widget(self.widget, _('Python Console'),
                                          PythonManager.get_interpreter_icon(), QtCore.Qt.BottomDockWidgetArea)
        dock.hide()
        dock.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Expanding)

    def close(self):
        self.widget.close()

    def apply_preferences(self):
        self.widget.font_name = settings.editor_font()
        self.widget.font_size = settings.editor_font_size()
        self.widget.syntax_highlighter.color_scheme = ColorScheme(settings.color_scheme())
        self.widget.update_terminal_colors()
