from PyQt5.QtWidgets import QTreeWidget

class NetworkDebugWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(["Time", "URL", "Status", "Duration"])
        self.setColumnCount(4)