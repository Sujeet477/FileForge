# FileForge

A simple and interactive File Management System built with Python. This project allows users to create, read, update, rename, and delete text files through a menu-driven interface.

## Features

* Create new text files
* Read file contents
* Rename existing files
* Overwrite file contents
* Append new content to files
* Delete files
* Automatic `.txt` extension handling
* Error handling using `try-except`
* User-friendly menu-driven interface

## Technologies Used

* Python 3
* pathlib
* os module

## Project Structure

```text
FileForge/
│
├── main.py
├── README.md
└── .gitignore (optional)
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Sujeet477/FileForge.git
```

2. Navigate to the project folder:

```bash
cd FileForge
```

3. Run the program:

```bash
python main.py
```

## Menu Options

```text
1. Create File
2. Read File
3. Update File
4. Delete File
```

## Example

### Create a File

```text
Please tell your response:- 1
Please tell your file name:- notes
What do you want to write in this file:- Hello World
File created successfully
```

### Read a File

```text
Please tell your response:- 2
Which file do you want to read:- notes.txt
Hello World
```

## Learning Outcomes

This project helped me practice:

* File Handling in Python
* Working with pathlib
* Exception Handling
* Functions and Modular Programming
* User Input Validation
* Basic CRUD Operations

## Future Improvements

* File search functionality
* File size display
* File creation/modification timestamps
* Graphical User Interface (GUI)
* Support for multiple file formats

## Author

**Sujeet Kumar**

GitHub: https://github.com/Sujeet477
