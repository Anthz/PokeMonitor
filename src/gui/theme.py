DARK_THEME = """
QMainWindow {
    background-color: #2d2d2d;
    color: #e0e0e0;
    font-family: 'Segoe UI';
}

QTabBar::tab {
    padding: 8px 12px;
    background: #353535;
    border: 1px solid #444;
}

QTabBar::tab:selected {
    background: #3a3a3a;
    border-bottom: 2px solid #4CAF50;
}

QTableWidget {
    gridline-color: #444;
    alternate-background-color: #2a2a2a;
}
"""

def apply_theme(app, theme_name="dark"):
    if theme_name == "dark":
        app.setStyleSheet(DARK_THEME)