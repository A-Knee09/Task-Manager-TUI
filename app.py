from textual.app import App, ComposeResult
from textual import events
from textual.widget import Widget
from textual.widgets import Static, Header, Footer
from textual.containers import Horizontal, Vertical


class TaskManager(App):
    """Class for creating the task manager"""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Task Manger App"


if __name__ == "__main__":
    app = TaskManager()
    app.run()
