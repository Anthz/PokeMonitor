from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QTableWidget, QGroupBox
)
from PyQt5.QtCore import Qt

class DashboardTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        # Stats Panel
        stats_group = QGroupBox("Monitoring Status")
        stats_layout = QHBoxLayout()
        
        self.status_label = QLabel("🟢 Active")
        self.product_count = QLabel("Products: 0")
        self.last_scan = QLabel("Last scan: Never")
        
        for widget in [self.status_label, self.product_count, self.last_scan]:
            stats_layout.addWidget(widget, alignment=Qt.AlignLeft)
        
        stats_group.setLayout(stats_layout)
        
        # Alerts Table
        self.alerts_table = QTableWidget(0, 3)
        self.alerts_table.setHorizontalHeaderLabels(["Product", "Price", "Time"])
        self.alerts_table.horizontalHeader().setStretchLastSection(True)
        
        layout.addWidget(stats_group)
        layout.addWidget(QLabel("Recent Alerts:"))
        layout.addWidget(self.alerts_table)
        self.setLayout(layout)