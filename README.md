# OS Fundamentals with Python

A completed beginner-friendly tutorial for Python's built-in `os` module.
The examples explain how programs work with folders, files, and paths through
small, runnable demonstrations.

## Tutorial status

The core tutorial is complete. The interactive examples currently cover:

- Current and changed working directories
- Relative, absolute, and normalized paths
- Listing and classifying files and directories
- Checking whether paths exist
- Creating single and nested directories
- Removing empty directories and understanding recursive deletion
- Removing and renaming files
- Reading file sizes
- Splitting file extensions and filtering files
- Reading file names and parent directories
- Joining paths safely across operating systems

The guide also explains `pathlib.Path` as a modern, object-oriented alternative
to `os.path`. It covers path joining, file and directory checks, directory
iteration, glob patterns, the difference between `os` and `pathlib`, and the
module-name collision that occurs when a user file is named `pathlib.py`.

It also includes a file-automation example in
[Automate_file.py](phase%20-%201%20Python%20Systems%20%26%20Automation%20Fundamentals/automate_file/Automate_file.py).
The script organizes files by extension using `os`, `os.path`, and `shutil`,
and explains the corrected `splitext()` typo and destination-folder logic.

For the detailed completion checklist and the next learning roadmap, see
[OS_LEARNING_GUIDE.md](phase%20-%201%20Python%20Systems%20%26%20Automation%20Fundamentals/os_fundamental/OS_LEARNING_GUIDE.md).

## Learning path

Start with the menu:

```bash
python os_tut.py
```

Or run a specific lesson:

```bash
python os_tut.py --lesson paths
python os_tut.py --lesson listing
python os_tut.py --lesson files
python os_tut.py --lesson system
python os_tut.py --lesson filter
python os_tut.py --lesson all
```

## Repository structure

```text
OS_fundamentals_python/
├── README.md      # Course overview, commands, and safety notes
├── phase - 1 Python Systems & Automation Fundamentals/
│   ├── os_fundamental/
│       ├── OS_LEARNING_GUIDE.md # Checklist, pathlib explanation, and comparison
│       ├── os_tut.py      # Interactive lesson runner and runnable examples
│       └── pathlib_demo.py # pathlib examples
│   └── automate_file/
│       └── Automate_file.py # Organizes files into folders by extension
└── .gitignore     # Python caches and local environment files
```

## What was learned

1. **Paths** - current, relative, and absolute paths; joining and splitting
   paths with `os.path`; normalizing paths with `os.path.normpath`.
2. **Directory inspection** - listing items and distinguishing files from
   directories.
3. **File operations** - creating directories, checking metadata, renaming,
   and removing files.
4. **Automation patterns** - finding files by extension, such as CSV files.
5. **File organization** - moving files into category folders based on their
   extensions with `shutil.move()`.

## Next steps

The core lessons are complete. The next planned topics are `os.walk()`,
`os.scandir()`, `os.stat()`, permissions, environment variables, processes,
`subprocess`, exception handling, and filesystem tests. The
[OS_LEARNING_GUIDE.md](phase%20-%201%20Python%20Systems%20%26%20Automation%20Fundamentals/os_fundamental/OS_LEARNING_GUIDE.md)
checklist tracks these topics and compares `os` with `pathlib`.

## Safety by design

Every mutating lesson creates a temporary directory with
`tempfile.TemporaryDirectory` and removes it automatically when the lesson
finishes. Running this tutorial will not create, rename, or delete files in
your project. The script also explains why `shutil.rmtree()` deserves extra
care: it recursively deletes a directory and everything inside it.

The examples use Python's standard library. Python 3.10 or newer is
recommended.
