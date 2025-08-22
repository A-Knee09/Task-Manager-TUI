from textual.app import App
from screens.menu import Menu
from screens.about import About
from screens.tasks import Tasks


class TaskManager(App):
    """Class for creating the task manager"""

    CSS_PATH = "./tcss/menu.tcss"

    def on_mount(self) -> None:

        self.theme = "flexoki"

        # Registering all the screens
        self.install_screen(Menu(), name="menu")
        self.install_screen(Tasks(), name="tasks")
        # self.install_screen(AddRemove(), name="add_remove")
        self.install_screen(About(), name="about")

        # On starting the app pushing the menu screen
        self.push_screen("menu")

        self.title = "Task Manager App"


if __name__ == "__main__":
    app = TaskManager()
    app.run()
