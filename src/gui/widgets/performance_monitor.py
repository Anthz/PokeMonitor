from PyQt5.QtWidgets import QWidget
from PyQt5 import QChart, QLineSeries

class PerformanceGraph(QWidget):
    """Realtime metrics graphing"""
    def __init__(self):
        super().__init__()
        self.chart = QChart()
        self.series = QLineSeries()
        self._setup_ui()