from PyQt5.QtCore import QSettings

class SettingsManager:
    def __init__(self):
        self.settings = QSettings("PokemonTCGMonitor", "Config")

    def save_window_state(self, window):
        self.settings.setValue("window_geometry", window.saveGeometry())
        self.settings.setValue("window_state", window.saveState())

    def load_window_state(self, window):
        if self.settings.value("window_geometry"):
            window.restoreGeometry(self.settings.value("window_geometry"))
        if self.settings.value("window_state"):
            window.restoreState(self.settings.value("window_state"))