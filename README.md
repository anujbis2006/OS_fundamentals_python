# OS Fundamentals with Python

An interactive, beginner-friendly guide to Python's built-in `os` module.
The examples explain how programs work with folders, files, paths, environment
variables, and basic system information.

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
├── os_tut.py      # Interactive lesson runner and runnable examples
└── .gitignore     # Python caches and local environment files
```

## What you will learn

1. **Paths** - current, relative, and absolute paths; joining and splitting
   paths with `os.path`.
2. **Directory inspection** - listing items and distinguishing files from
   directories.
3. **File operations** - creating directories, checking metadata, renaming,
   and removing files.
4. **System context** - reading environment variables and platform details.
5. **Automation patterns** - finding files by extension, such as CSV files.

## Safety by design

Every mutating lesson creates a temporary directory with
`tempfile.TemporaryDirectory` and removes it automatically when the lesson
finishes. Running this tutorial will not create, rename, or delete files in
your project. The script also explains why `shutil.rmtree()` deserves extra
care: it recursively deletes a directory and everything inside it.

The examples use only Python's standard library. Python 3.10 or newer is
recommended.
