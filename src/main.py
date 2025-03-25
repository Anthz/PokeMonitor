import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.theme import apply_theme

def main():
    app = QApplication(sys.argv)
    apply_theme(app, "dark")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()