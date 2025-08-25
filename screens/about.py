from textual.screen import Screen
from textual.containers import Container, Horizontal, Vertical
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer


class About(Screen):
    """Class representing the about me screen"""

    CSS_PATH = "../tcss/about.tcss"

    BINDINGS = [
        ("q", "quit_app", "Quit the application"),
        ("m", "menu", "Go to the menu"),
    ]

    def compose(self) -> ComposeResult:

        AVATAR = """
   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿⣿⠛⣿⣿⣿⣿⡏⡻⣿⣿⣿⣿⣿⡇⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿⣿⡌⢮⣟⣻⡻⡷⠘⢮⣝⣛⠿⠿⠇⢧⠸⠟⢛⡉⢉⣩⣽⣿⣿⣿
   ⣿⣿⣿⣿⣿⡷⢈⣩⣽⣿⣿⣶⣬⣿⣿⣿⣷⣦⣧⣾⡟⢡⣿⣿⣿⣿⣿⣿
   ⣿⡟⠫⡭⠶⠚⣛⣫⣽⡿⢛⣿⠟⡩⢋⣽⣿⣿⣿⣿⣷⣜⠻⣿⣿⣿⣿⣿
   ⣿⣿⡷⢒⣴⠞⠡⣿⠏⣰⡿⢣⠊⠐⣸⠏⣽⠘⣏⢻⡟⣿⠃⡒⠭⣍⣫⡿
   ⣿⠟⠑⠋⠀⡁⠚⠁⠀⠈⠁⢃⡔⣸⡟⠘⠛⠀⠻⠄⣷⢹⣷⢁⢶⣶⣶⣾
   ⣧⣤⡾⠀⠊⢌⠀⠀⠀⠀⠀⢈⣁⡉⠀⠀⠀⠀⠀⠀⡟⠈⠿⠘⠘⣿⣿⣿
   ⣿⣿⠁⣴⣾⣿⣷⣤⣤⣤⣶⣿⣿⣿⣤⣀⣀⣀⣀⣠⡐⠀⠖⢀⣤⠌⢙⣿
   ⣿⣿⡀⠙⠿⣿⣿⣿⣿⡀⢶⣶⣶⠆⣹⣿⣿⣿⣿⣿⡷⠂⢀⣀⣤⣶⣿⣿
   ⣿⣿⣿⣷⣶⣤⣭⣉⣙⣛⠒⠲⠶⠾⠟⠛⢛⣩⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
        """

        self.styles.background = "#0d1117"
        # yield Header()
        yield Footer()
        yield Container(id="shadow")

        with Container(id="about_me"):
            with Container(id="column1"):
                yield Static(AVATAR, id="avatar")

            with Vertical(id="my_desc"):
                yield Static(
                    "[cornflowerblue]Name[/cornflowerblue]: Anirudh Saksena (A-knee)"
                )
                yield Static("[cornflowerblue]Age[/cornflowerblue]: 22")
                yield Static(
                    "[cornflowerblue]Edu[/cornflowerblue]: Masters in Computer Applications"
                )
                yield Static(
                    "[cornflowerblue]Interests[/cornflowerblue]: I play a lot of video games"
                )

    def on_mount(self) -> None:

        about_me_border = self.query_one("#about_me")
        about_me_border.border_title = "[b]About Me[/b]"
        about_me_border.styles.border_title_align = "left"
        about_me_border.styles.border_title_color = "orange"

    def on_resize(self) -> None:
        """Handle screen resize events"""
        self.adjust_layout()

    def adjust_layout(self) -> None:
        """Adjusting layout based on current terminal size"""
        width, height = self.size

        about_me = self.query_one("#about_me")
        shadow = self.query_one("#shadow")

        # Adjustments based on terminal width
        if width < 80:
            # Small terminal
            about_me.styles.width = "90%"
            about_me.styles.height = "70%"
            shadow.styles.width = "90%"
            shadow.styles.height = "70%"
        elif width < 120:
            # Medium terminal
            about_me.styles.width = "70%"
            about_me.styles.height = "60%"
            shadow.styles.width = "70%"
            shadow.styles.height = "60%"
        else:
            # Large terminal
            about_me.styles.width = "50%"
            about_me.styles.height = "50%"
            shadow.styles.width = "50%"
            shadow.styles.height = "50%"

    async def action_quit_app(self):
        self.app.exit()

    async def action_menu(self) -> None:
        await self.app.push_screen("menu")
