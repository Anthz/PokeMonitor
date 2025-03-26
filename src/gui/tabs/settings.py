from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QCheckBox, QSpinBox, QGroupBox, QLabel
)
from src.utils.debug import DebugManager

class SettingsTab(QWidget):
    def __init__(self, debug_manager: DebugManager):
        super().__init__()
        self.debug_manager = debug_manager
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()
        
        # Debug Group
        debug_group = QGroupBox("Debug Settings")
        debug_layout = QVBoxLayout()
        
        self.debug_toggle = QCheckBox("Enable Debug Mode")
        self.debug_toggle.setChecked(self.debug_manager.enabled)
        self.debug_toggle.stateChanged.connect(
            lambda: self.debug_manager.set_enabled(self.debug_toggle.isChecked())
        )
        
        self.verbosity = QSpinBox()
        self.verbosity.setRange(1, 3)  # 1=Basic, 2=Detailed, 3=Verbose
        self.verbosity.setValue(2)
        
        debug_layout.addWidget(self.debug_toggle)
        debug_layout.addWidget(QLabel("Verbosity Level:"))
        debug_layout.addWidget(self.verbosity)
        debug_group.setLayout(debug_layout)
        
        layout.addWidget(debug_group)
        layout.addStretch()
        self.setLayout(layout)