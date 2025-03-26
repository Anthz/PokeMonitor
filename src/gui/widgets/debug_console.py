from PyQt5.QtWidgets import (
    QWidget, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt, pyqtSlot
from datetime import datetime

class DebugConsole(QWidget):
    def __init__(self, debug_manager):
        super().__init__()
        self.debug_manager = debug_manager
        self._setup_ui()
        self.debug_manager.debug_updated.connect(self._append_log)

    def _setup_ui(self):
        layout = QVBoxLayout()
        
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.setStyleSheet("""
            font-family: monospace;
            background-color: #1e1e1e;
            color: #d4d4d4;
        """)
        
        # Toolbar
        toolbar = QHBoxLayout()
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.console.clear)
        
        self.save_btn = QPushButton("Save Log")
        self.save_btn.clicked.connect(self._save_log)
        
        toolbar.addWidget(self.clear_btn)
        toolbar.addWidget(self.save_btn)
        
        layout.addLayout(toolbar)
        layout.addWidget(self.console)
        self.setLayout(layout)

    @pyqtSlot(str)
    def _append_log(self, message: str):
        """Add new debug message to console"""
        self.console.append(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
        self.console.ensureCursorVisible()

    def _save_log(self):
        """Save debug log to file"""
        with open("debug_log.txt", "w") as f:
            f.write(self.console.toPlainText())