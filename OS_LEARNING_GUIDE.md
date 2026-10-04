# Python OS Learning Guide

> An interactive checklist for learning Python's `os` module.
>
> Mark a box with `[x]` after you understand the concept and can explain it
> without copying the example. Add notes or new topics as the course grows.

## Current status

**Core tutorial completed:** Parts 1–5 are complete. The advanced topics in
Part 6 are the next stage of learning.

The completed tutorial now covers:

- Working directories and safe temporary practice workspaces
- Listing and classifying files and directories
- Creating and removing directories
- Removing and renaming files
- File sizes and extensions
- File names, parent directories, joined paths, absolute paths, and normalized
  paths

## How to use this guide

1. Read one topic at a time.
2. Run the related example in `os_tut.py`.
3. Change the example and observe what happens.
4. Mark the topic complete only when you can describe **what it does**, **why
   it is useful**, and **what can go wrong**.
5. Add your own notes below each topic.

---

## Part 1: Understanding the current location

### 1. Current working directory

- [x] Understand what a current working directory means.
- [x] Use `os.getcwd()` to display the directory where Python is running.
- [x] Explain why a relative path is interpreted from the current directory.

**My notes:**

<!-- Add your explanation here. -->

### 2. Changing the current working directory

- [x] Use `os.chdir(path)` to move to another directory.
- [x] Verify the change with `os.getcwd()`.
- [x] Understand that `os.chdir()` changes process-wide state.
- [x] Know why a program should validate a path before calling `os.chdir()`.

**My notes:**

<!-- Add your explanation here. -->

---

## Part 2: Reading a directory

### 3. Listing files and folders

- [x] Use `os.listdir()` for the current directory.
- [x] Use `os.listdir(path)` for a specific directory.
- [x] Loop over the returned names.
- [x] Understand that `os.listdir()` returns names, not complete paths.
- [x] Build a complete path with `os.path.join()`.

**Try it:**

- [x] List all entries in a practice folder.
- [x] Print each entry on its own line.
- [x] Find only the entries with a `.csv` extension.

**My notes:**

<!-- Add your explanation here. -->

### 4. Checking whether something exists

- [x] Use `os.path.exists(path)`.
- [x] Write an `if/else` check for an optional file such as `config.json`.
- [x] Understand that a path can exist as either a file or a directory.

**My notes:**

<!-- Add your explanation here. -->

### 5. Distinguishing files and directories

- [x] Use `os.path.isfile(path)`.
- [x] Use `os.path.isdir(path)`.
- [x] Classify every entry returned by `os.listdir()`.
- [x] Understand why checking the type before an operation prevents errors.

**My notes:**

<!-- Add your explanation here. -->

---

## Part 3: Creating and removing directories

### 6. Creating one directory with `os.mkdir()`

- [x] Create one new directory with `os.mkdir(path)`.
- [x] Understand that it raises `FileExistsError` if the directory already
  exists.
- [x] Check for existence before creating a directory when appropriate.

**My notes:**

<!-- Add your explanation here. -->

### 7. Creating nested directories with `os.makedirs()`

- [x] Create multiple levels with `os.makedirs(path)`.
- [x] Use `exist_ok=True` when an existing directory is acceptable.
- [x] Explain the difference between `os.mkdir()` and `os.makedirs()`.

**Practice tree:**

```text
data/
└── reports/
    └── 2026/
```

- [x] Create the practice tree.
- [x] Confirm each level with `os.path.isdir()`.

### 8. Removing an empty directory

- [x] Use `os.rmdir(path)` for an empty directory.
- [x] Understand why `os.rmdir()` fails when the directory contains files.
- [x] Remove child directories before their parent directory.

**My notes:**

<!-- Add your explanation here. -->

### 9. Removing a directory recursively

- [x] Explain what `shutil.rmtree(path)` does.
- [x] Understand that it removes the directory and all of its contents.
- [x] Never run it on a path you have not checked carefully.
- [x] Practice only inside a temporary test directory.

> **Safety rule:** Recursive deletion is powerful and irreversible. Prefer
> `os.rmdir()` for empty directories and validate every destructive path.

---

## Part 4: Managing files

### 10. Removing a file

- [x] Use `os.remove(path)`.
- [x] Check `os.path.exists(path)` before removal when the file is optional.
- [x] Understand the difference between removing a file and removing a
  directory.

**My notes:**

<!-- Add your explanation here. -->

### 11. Renaming a file or directory

- [x] Use `os.rename(old_path, new_path)`.
- [x] Understand that renaming can also move an item when the destination
  directory is different.
- [x] Check that the source exists before renaming.

**My notes:**

<!-- Add your explanation here. -->

### 12. Reading file size

- [x] Use `os.path.getsize(path)`.
- [x] Understand that the result is measured in bytes.
- [x] Convert bytes to KB, MB, or GB.
- [x] Explain why a missing path causes an error.

**Conversion notes:**

```text
KB = bytes / 1024
MB = bytes / (1024 * 1024)
GB = bytes / (1024 * 1024 * 1024)
```

---

## Part 5: Understanding file names and paths

### 13. Splitting a file extension

- [x] Use `os.path.splitext(filename)`.
- [x] Separate the file name from its extension.
- [x] Filter files such as `.txt`, `.csv`, and `.pdf`.
- [x] Compare extensions consistently, for example with `.lower()`.

**My notes:**

<!-- Add your explanation here. -->

### 14. Reading the file name from a path

- [x] Use `os.path.basename(path)`.
- [x] Explain why the basename is useful when displaying a file to a user.

### 15. Reading the parent directory from a path

- [x] Use `os.path.dirname(path)`.
- [x] Explain how it identifies the directory containing the item.

### 16. Joining paths safely

- [x] Use `os.path.join("data", "users.csv")`.
- [x] Understand why string concatenation such as `"data/" + "users.csv"` is
  less portable.
- [x] Know that path separators differ between operating systems.

**My notes:**

<!-- Add your explanation here. -->

### 17. Relative and absolute paths

- [x] Define a relative path.
- [x] Define an absolute path.
- [x] Use `os.path.abspath(path)` to create an absolute path.
- [x] Explain when each kind of path is useful.
- [x] Normalize a path with `os.path.normpath(path)`.

---

## Part 6: Topics to learn next

These topics are not covered in the current lesson yet. Add them one at a
time as new examples are created.

- [ ] `os.walk()` for recursively reading a directory tree.
- [ ] `os.scandir()` for efficient directory inspection.
- [ ] `os.stat()` for detailed file metadata.
- [ ] File permissions with `os.access()`.
- [ ] Environment variables with `os.environ` and `os.getenv()`.
- [ ] Platform information with `os.name` and `platform`.
- [ ] Running external commands with `os.system()` and why `subprocess` is
  usually safer.
- [ ] Process information such as `os.getpid()`.
- [ ] Working with `pathlib.Path` as a modern alternative to `os.path`.
- [ ] Handling `FileNotFoundError`, `PermissionError`, and
  `FileExistsError`.
- [ ] Writing tests for filesystem code with temporary directories.

---

## Progress tracker

| Section | Status | Notes |
| --- | --- | --- |
| Current location | Complete | |
| Reading directories | Complete | |
| Creating/removing directories | Complete | |
| Managing files | Complete | |
| File names and paths | Complete | |
| Next topics | Not started | |

### Questions to answer before moving on

- [x] What is the difference between a file path and a file object?
- [x] Why should paths be joined instead of concatenated?
- [x] Why can `os.rmdir()` remove only empty directories?
- [x] What makes `shutil.rmtree()` dangerous?
- [x] How would you process every CSV file inside a folder safely?
