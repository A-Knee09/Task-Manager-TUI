"""
Note for me:
self.data_table.cursor_coordinate → current cell's coordinate (row, column).
coordinate_to_cell_key() → maps that coordinate to the actual row key and column key in the DataTable.
"""

from textual.app import ComposeResult
from textual.widgets import Static, DataTable, Header, Footer, Input, Checkbox
from textual.screen import Screen
from textual.containers import Container
from rich.text import Text


class Tasks(Screen):
    """Class to handle the tasks screen"""

    CSS_PATH = "../tcss/tasks.tcss"
    BINDINGS = [
        ("a", "add_tasks", "Add a task"),
        ("r", "remove_tasks", "Remove a task"),
        ("u", "update_task", "Update a task"),
        ("m", "menu", "Menu"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:

        yield Header()
        yield Footer()

        with Container(id="tasks_container"):

            # TITLE
            yield Static(
                "[b][cornflowerblue]TUI Task Manager - Tasks[/cornflowerblue][/b]",
                id="title",
            )

            # Tasks Table
            self.data_table = DataTable(id="table")
            self.data_table.add_columns("Task No.", "Task")
            self.data_table.cursor_type = "row"
            self.data_table.zebra_stripes = True

            yield self.data_table

    async def action_add_tasks(self):
        """
        yield in action_add_tasks won’t work because compose() runs only once during initial rendering.
        Using self.mount(widget) to add widgets dynamically after the screen has been rendered
        """

        input_box = Input(placeholder="Enter a task")
        await self.mount(input_box, after=self.data_table)
        input_box.focus()

    def on_input_submitted(self, event: Input.Submitted):
        """Handle the input Submitted and update the table"""
        task_text = event.value.strip()
        if task_text:
            task_no = self.data_table.row_count + 1
            self.data_table.add_row(str(task_no), task_text)

        # Remove input after submission
        event.input.remove()

    async def action_menu(self) -> None:
        await self.app.push_screen("menu")

    async def action_remove_tasks(self) -> None:
        row_key, _ = self.data_table.coordinate_to_cell_key(
            self.data_table.cursor_coordinate
        )
        self.data_table.remove_row(row_key)

    async def action_quit(self):
        self.app.exit()
