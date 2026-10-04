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

For the detailed completion checklist and the next learning roadmap, see
[OS_LEARNING_GUIDE.md](OS_LEARNING_GUIDE.md).

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
├── OS_LEARNING_GUIDE.md # Completed checklist and future topics
├── os_tut.py      # Interactive lesson runner and runnable examples
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

## Next steps

The core lessons are complete. The next planned topics are `os.walk()`,
`os.scandir()`, `os.stat()`, permissions, environment variables, processes,
`subprocess`, `pathlib`, exception handling, and filesystem tests. The
checklist in [OS_LEARNING_GUIDE.md](OS_LEARNING_GUIDE.md) tracks these topics.

## Safety by design

Every mutating lesson creates a temporary directory with
`tempfile.TemporaryDirectory` and removes it automatically when the lesson
finishes. Running this tutorial will not create, rename, or delete files in
your project. The script also explains why `shutil.rmtree()` deserves extra
care: it recursively deletes a directory and everything inside it.

The examples use Python's standard library. Python 3.10 or newer is
recommended.
