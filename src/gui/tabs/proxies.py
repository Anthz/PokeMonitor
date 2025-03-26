# src/gui/tabs/proxies.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QTextEdit, QComboBox, QLabel, QPushButton
class ProxiesTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        # Proxy Source Tabs
        self.source_tabs = QTabWidget()
        
        # Manual Entry
        manual_tab = QWidget()
        manual_layout = QVBoxLayout()
        self.proxy_textedit = QTextEdit()
        self.proxy_textedit.setPlaceholderText("Enter one proxy per line...")
        manual_layout.addWidget(self.proxy_textedit)
        manual_tab.setLayout(manual_layout)
        
        # API Sources
        api_tab = QWidget()
        api_layout = QVBoxLayout()
        self.api_combo = QComboBox()
        self.api_combo.addItems(["Luminati", "Smartproxy", "Custom"])
        api_layout.addWidget(QLabel("Proxy Provider:"))
        api_layout.addWidget(self.api_combo)
        api_tab.setLayout(api_layout)
        
        self.source_tabs.addTab(manual_tab, "Manual")
        self.source_tabs.addTab(api_tab, "API")
        
        # Test Button
        self.test_btn = QPushButton("Test All Proxies")
        
        layout.addWidget(self.source_tabs)
        layout.addWidget(self.test_btn)
        self.setLayout(layout)