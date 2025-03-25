from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QHeaderView
)
from PyQt5.QtCore import Qt
import yaml
import os

class ProductsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        # Toolbar
        toolbar = QHBoxLayout()
        self.add_btn = QPushButton("Add Product")
        self.import_btn = QPushButton("Import")
        self.export_btn = QPushButton("Export")
        
        for btn in [self.add_btn, self.import_btn, self.export_btn]:
            toolbar.addWidget(btn)
        
        # Product Table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Target Price", "Keywords"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Load existing products
        self._load_products()
        
        layout.addLayout(toolbar)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def _load_products(self):
        if not os.path.exists("config/products.yaml"):
            return
            
        with open("config/products.yaml") as f:
            products = yaml.safe_load(f) or []
            
        self.table.setRowCount(len(products))
        for i, product in enumerate(products):
            self.table.setItem(i, 0, QTableWidgetItem(product['name']))
            self.table.setItem(i, 1, QTableWidgetItem(str(product['target_price'])))
            self.table.setItem(i, 2, QTableWidgetItem(", ".join(product['keywords'])))