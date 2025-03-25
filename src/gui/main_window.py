from PyQt5.QtWidgets import (
    QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QStatusBar
)
from .tabs.dashboard import DashboardTab
from .tabs.products import ProductsTab
from .tabs.proxies import ProxiesTab
from .settings_manager import SettingsManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = SettingsManager()
        self.setWindowTitle("Pokémon TCG Monitor")
        self.resize(1200, 800)
        
        # Central Tab System
        self.tabs = QTabWidget()
        self._setup_tabs()
        self.setCentralWidget(self.tabs)
        
        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Load saved state
        self.settings.load_window_state(self)

    def _setup_tabs(self):
        """Initialize all application tabs"""
        self.tabs.addTab(DashboardTab(), "🏠 Dashboard")
        self.tabs.addTab(ProductsTab(), "📦 Products")
        self.tabs.addTab(ProxiesTab(), "🔒 Proxies")

    def closeEvent(self, event):
        self.settings.save_window_state(self)
        super().closeEvent(event)