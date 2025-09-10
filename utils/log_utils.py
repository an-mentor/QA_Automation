from datetime import datetime

class Logger:
    @staticmethod
    def _log(level: str, message: str):
        """Centralized logger with timestamp + level."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")

    @staticmethod
    def log_console(page):
        def on_console(msg):
            if msg.type == "error":
                loc = msg.location or {}
                url = loc.get("url") or ""
                line = loc.get("lineNumber") or ""
                col = loc.get("columnNumber") or ""
                Logger._log("console:error",
                            f"{msg.text} ({url}:{line}:{col})")
        page.on("console", on_console)

    @staticmethod
    def log_page_errors(page):
        def on_page_error(error):
            Logger._log("pageerror", str(error))
        page.on("pageerror", on_page_error)

    @staticmethod
    def log_dialogs(page):
        def on_dialog(dialog):
            Logger._log("dialog", f"[{dialog.type}] {dialog.message}")
            try:
                dialog.accept()
                Logger._log("dialog", "accepted")
            except Exception as e:
                Logger._log("dialog", f"error handling dialog: {e}")
        page.on("dialog", on_dialog)
