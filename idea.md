# MVP Task Manager (Textual TUI)
---
## Core Features

* 1.Menu Screen – Choose:

  * View tasks

  * Add/remove tasks

  * About

  * Quit

* 2. Task Screen – Show a simple list of tasks.

* 3.Add/Remove Screen – Add a new task or remove by index.

* 4. No file storage yet – Tasks are stored in a Python list.
---
## File Structure
```bash
task_manager/
│
├── app.py             # Entry point, initializes Textual app
├── screens/
│   ├── menu.py        # Menu screen (main navigation)
│   ├── tasks.py       # View tasks screen
│   ├── add_remove.py  # Add/Remove tasks screen
│   └── about.py       # About screen
└── state.py           # Holds global task list for now
```
---
## Role of Each File

* app.py

  * Imports Textual App class.

  * Loads menu screen as the first screen.

  * Handles navigation between screens.

* screens/menu.py

  * Displays menu options.

  * Captures keypress or selection to navigate.

* screens/tasks.py

  * Displays list of tasks from state.py.

* screens/add_remove.py

  * Provides simple UI to:

    * Add task (append to list)

    * Remove task (by index)

* screens/about.py

  * Shows basic app info.

* state.py

  * Contains global tasks = [] list.

  * Other screens can import and modify it.
---
## Flow

* 1. User starts app → menu.py shows.

* 2. Press `t` → Go to tasks.py → Shows current tasks.

* 3. Press `r` → Go to add_remove.py → Add or remove.

* 4. Press `a` → Go to about.py → Info screen.

* 5. Press `e` → Exit.
---

