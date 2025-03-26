from PyQt5.QtWidgets import QSplitter, QTreeWidget, QTextEdit
from PyQt5.QtCore import Qt

class DOMExplorer(QSplitter):
    """Live DOM tree viewer for Selenium sessions"""
    def __init__(self, driver):
        super().__init__(Qt.Horizontal)
        self.tree = QTreeWidget()
        self.html_view = QTextEdit()
        self._update_dom(driver.page_source)