import PyQt5
from PyQt5.QtWidgets import (
    QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QStatusBar, QDockWidget, QAction
)
from PyQt5.QtCore import Qt

from src.gui.widgets.debug_console import DebugConsole
from src.utils.debug import DebugManager
from src.gui.tabs.dashboard import DashboardTab
from src.gui.tabs.products import ProductsTab
from src.gui.tabs.proxies import ProxiesTab
from src.gui.settings_manager import SettingsManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize settings manager
        self.settings = SettingsManager()

        # Initialize debug system
        self.debug = DebugManager()
        
        # Add debug console as dock widget
        self.debug_dock = QDockWidget("Debug Console", self)
        self.debug_dock.setWidget(DebugConsole(self.debug))
        self.addDockWidget(Qt.BottomDockWidgetArea, self.debug_dock)
        self.debug_dock.setVisible(False)  # Hidden by default
        
        # Create View menu
        self.view_menu = self.menuBar().addMenu("View")

        # Toggle debug console in View menu
        toggle_debug = QAction("Debug Console", self)
        toggle_debug.setCheckable(True)
        toggle_debug.triggered.connect(self.debug_dock.setVisible)
        self.view_menu.addAction(toggle_debug)

        # Initialize tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self._setup_tabs()

    def _setup_tabs(self):
        """Initialize all application tabs"""
        self.tabs.addTab(DashboardTab(), "🏠 Dashboard")
        self.tabs.addTab(ProductsTab(), "📦 Products")
        self.tabs.addTab(ProxiesTab(), "🔒 Proxies")

    def closeEvent(self, event):
        self.settings.save_window_state(self)
        super().closeEvent(event)