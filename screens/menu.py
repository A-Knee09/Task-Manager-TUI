import pyfiglet as pf
from textual.app import App, ComposeResult
from textual.containers import Container, HorizontalScroll, Vertical, Horizontal
from textual.widgets import Static


class Menu(App):

    CSS_PATH = "../tcss/menu.tcss"

    BINDINGS = [
        ("t", "see_tasks", "Goes to the tasks"),
        ("r", "add_remove_tasks", "Add and remove tasks screens"),
        ("a", "about_me", "Stuff about me and the app"),
        ("q", "quit_app", "quits the app"),
    ]

    def compose(self) -> ComposeResult:

        with Container(id="menu_container"):
            with Horizontal(id="menu_title"):
                ascii_title = pf.figlet_format("TUI Task Manager", font="larry3d")
                yield Static(ascii_title)

            icons = ["", "", "", "󰩈"]
            menu_items = [
                ("See tasks", "t"),
                ("Add/Remove Tasks", "r"),
                ("About Me", "a"),
                ("Quit", "q"),
            ]
            with Vertical(id="menu_options"):
                for (option, key), icon in zip(menu_items, icons):
                    yield Static(
                        f"{icon}  {option:<50} [bold orange]{key}[/bold orange]\n"
                    )


if __name__ == "__main__":

    menu = Menu()
    menu.run()
