"""
Note for me:
self.data_table.cursor_coordinate → current cell's coordinate (row, column).
coordinate_to_cell_key() → maps that coordinate to the actual row key and column key in the DataTable.
"""

from textual.app import ComposeResult
from textual.widgets import Static, DataTable, Footer, Input
from textual.screen import Screen
from textual.containers import Container


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

        # yield Header()
        yield Footer()

        with Container(id="tasks_container"):

            yield Static(
                "[b][cornflowerblue]TUI Task Manager - Tasks[/cornflowerblue][/b]",
                id="title",
            )

            # Tasks Table
            self.data_table = DataTable(id="table")
            self.data_table.add_columns("Task No.", "Task")
            self.data_table.cursor_type = "cell"
            self.data_table.cell_padding = 17
            # self.data_table.zebra_stripes = True

            yield self.data_table

    async def action_add_tasks(self):
        """Trigger add task mode"""
        self.update_mode = False  # Adding new task
        input_box = Input(placeholder="Enter a task")
        await self.mount(input_box, after=self.data_table)
        input_box.focus()

    async def action_update_task(self):
        """Trigger update task mode"""
        row_key, column_key = self.data_table.coordinate_to_cell_key(
            self.data_table.cursor_coordinate
        )
        self.edit_row_key = row_key
        self.edit_column_key = column_key
        self.update_mode = True  # Updating existing task

        input_box = Input(placeholder="Update the task")
        await self.mount(input_box, after=self.data_table)
        input_box.focus()

    def on_input_submitted(self, event: Input.Submitted):
        """Handle both adding and updating"""
        value = event.value.strip()
        if not value:
            event.input.remove()
            return

        if getattr(self, "update_mode", False):
            # Update existing task
            self.data_table.update_cell(self.edit_row_key, self.edit_column_key, value)
        else:
            # Add new task
            task_no = self.data_table.row_count + 1
            self.data_table.add_row(str(task_no), value)

        event.input.remove()

    async def action_remove_tasks(self):
        """Remove selected task"""
        row_key, _ = self.data_table.coordinate_to_cell_key(
            self.data_table.cursor_coordinate
        )
        self.data_table.remove_row(row_key)

    async def action_menu(self) -> None:
        await self.app.push_screen("menu")

    async def action_quit(self):
        self.app.exit()
