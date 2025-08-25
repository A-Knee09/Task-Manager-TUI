# To Do List TUI (WIP)

A terminal-based task management application built with [Textual](https://textual.textualize.io/).  
Currently in development – core features like adding, updating, and removing tasks are functional, with more planned.

## Features (So Far)
- Add new tasks quickly  
- Update existing tasks  
- Remove tasks with a single key press  
- Simple keyboard navigation  

## Screenshots
*(Development Build)* 

### 1. Main Menu
<img width="1920" height="1080" alt="swappy-20250826-001601" src="https://github.com/user-attachments/assets/96993377-f606-43c3-b300-151db710cd07" />


### 2. Tasks Screen
<img width="1920" height="1080" alt="swappy-20250825-235233" src="https://github.com/user-attachments/assets/b1bae624-cce0-42a6-a38c-a03921c2f662" />

### 3. About Me Screen
<img width="1920" height="1080" alt="swappy-20250825-235251" src="https://github.com/user-attachments/assets/95b5361c-7b66-4604-8a87-4eda1f700410" />



## How to run

### Clone the Repository

```bash
# Clone the repository
git clone https://github.com/A-Knee09/To-do-TUI.git
cd Task-Manager-TUI
```

### Create and Activate Virtual Environment

#### On Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

### Run the Application

```bash
python3 app.py  # For linux
#OR 
textual run app.py --dev
```
