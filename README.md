CLI File Manager

A simple command-line file manager built with Python.

Project: CLI_FILE_MANAGER
Created by: DashMC

About

CLI File Manager is a Python program that allows users to manage files and folders through command-line commands.

You can create, copy, delete and rename files. It also includes a simple Tkinter window for viewing files in a selected folder.

The program works with a folder path provided by the user.

Requirements

The original project includes the following files:

- "CLI_ARCHIVE_HANDLER.py"
- "CLI_CONFIG.py"
- "CLI_LOGGER.py"
- "CLI_MAIN.py"
- "GLOBAL_ROUTE.py"
- "OWN_FORMATTER.py"

The original instructions also mention the "__pycache__" folder and required archive files.

Keep the required project files together in the same folder.

How to Run

First, open a terminal in the project folder.

Run the main Python file and provide the folder path you want to access.

For example:

python CLI_MAIN.py "C:/MY_carpet"

The folder path should be provided as the first argument.

After that, you can use the available commands to manage files.

Available Commands

1. Create a File

Command: "-cr" or "--create"

Creates a new file inside the selected folder.

You need to provide the filename and its extension.

Example:

--create text txt

Result:

text.txt

2. Copy a File

Command: "-co" or "--copy"

Copies a file from one location to another.

You need to provide the source file and the destination folder.

If the file is already inside the folder selected when starting the program, you can provide its filename directly.

The program creates another copy when a file with the same name already exists in the destination folder.

3. Delete a File

Command: "-de" or "-delete"

Deletes a file from the selected folder.

Example:

-de text.txt

4. Rename or Move a File

Command: "-re" or "--rename"

Renames a file using its current name and its new name.

Example:

-re text.txt text2.txt

Result:

text2.txt

This command can also be used to move files.

Note: Include the file extension in the new name. Otherwise, the resulting filename may not be what you expect.

5. View Files

Command: "-vi" or "--view"

Opens a simple Tkinter window that displays files from the selected folder.

You need to provide the file extension you want to view.

Examples:

- "txt" — Displays text files.
- "folder" — Displays folders.

The original instructions indicate that this command works with the initially selected folder.

Help

To see information about the available commands, use:

--help

That's All!

These are the main commands available in CLI File Manager.

Explore the commands, manage your files and folders, and enjoy using the program!

Thanks for checking out this project.

Made by DashMC.
