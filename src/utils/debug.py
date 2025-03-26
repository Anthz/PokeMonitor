import logging
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from typing import Optional, Dict, Any

class DebugManager(QObject):
    debug_updated = pyqtSignal(str)  # Signal for GUI updates
    
    def __init__(self):
        super().__init__()
        self._enabled = False
        self._log_level = logging.INFO
        self._activity_buffer = []
        self.setup_logger()

    def setup_logger(self):
        """Configure Python logging to integrate with our debug system"""
        logging.basicConfig(
            level=self._log_level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[DebugLogHandler(self)]
        )

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, state: bool):
        self._enabled = state
        self._log_level = logging.DEBUG if state else logging.INFO
        logging.getLogger().setLevel(self._log_level)
        self.log(f"Debug mode {'enabled' if state else 'disabled'}")

    def log(self, 
           message: str, 
           level: str = "info",
           data: Optional[Dict[str, Any]] = None):
        """Centralized logging method"""
        if not self._enabled and level == "debug":
            return
            
        entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "level": level.upper(),
            "data": data or {}
        }
        
        # Store in circular buffer (last 1000 entries)
        self._activity_buffer = (self._activity_buffer + [entry])[-1000:]
        
        # Emit to GUI
        self.debug_updated.emit(message)
        
        # Standard logging
        getattr(logging, level)(f"{message} | Data: {data}")

    def get_recent_activities(self, limit: int = 50) -> list:
        return self._activity_buffer[-limit:]

class DebugLogHandler(logging.Handler):
    """Bridges Python logging to our debug system"""
    def __init__(self, debug_manager: DebugManager):
        super().__init__()
        self.debug_manager = debug_manager

    def emit(self, record):
        self.debug_manager.log(
            record.getMessage(),
            record.levelname.lower(),
            {"file": record.pathname, "line": record.lineno}
        )