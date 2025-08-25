import pyfiglet as pf
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Static, Header, Footer


class Menu(Screen):
    """Class representing the menu screen"""

    CSS_PATH = "../tcss/menu.tcss"

    BINDINGS = [
        ("t", "see_tasks", "Goes to the tasks"),
        ("a", "about_me", "Some Yap about me"),
        ("q", "quit_app", "Quit the app"),
    ]

    def compose(self) -> ComposeResult:

        yield Header()
        yield Footer()

        with Container(id="menu_container"):
            with Horizontal(id="menu_title"):
                ascii_title = pf.figlet_format("TUI Task Manager", font="larry3d")
                yield Static(ascii_title)

            icons = ["", "", "󰩈"]
            menu_items = [
                ("See tasks", "t"),
                ("About Me", "a"),
                ("Quit", "q"),
            ]
            with Vertical(id="menu_options"):
                for (option, key), icon in zip(menu_items, icons):
                    yield Static(
                        f"{icon}  {option:<50} [bold orange]{key}[/bold orange]\n"
                    )

    async def action_see_tasks(self):
        await self.app.push_screen("tasks")

    async def action_add_remove(self):
        await self.app.push_screen("add_remove")

    async def action_about_me(self):
        await self.app.push_screen("about")

    async def action_quit_app(self):
        self.app.exit()
