class ScraperConfigWidget(QWidget):
    def __init__(self, scraper_class):
        self.strategy_table = QTableWidget()
        for strategy in scraper_class.get_selector_strategies():
            self._add_strategy_row(strategy)