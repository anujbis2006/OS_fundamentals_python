# Python OS Learning Guide

> An interactive checklist for learning Python's `os` module.
>
> Mark a box with `[x]` after you understand the concept and can explain it
> without copying the example. Add notes or new topics as the course grows.

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

- [ ] Understand what a current working directory means.
- [ ] Use `os.getcwd()` to display the directory where Python is running.
- [ ] Explain why a relative path is interpreted from the current directory.

**My notes:**

<!-- Add your explanation here. -->

### 2. Changing the current working directory

- [ ] Use `os.chdir(path)` to move to another directory.
- [ ] Verify the change with `os.getcwd()`.
- [ ] Understand that `os.chdir()` changes process-wide state.
- [ ] Know why a program should validate a path before calling `os.chdir()`.

**My notes:**

<!-- Add your explanation here. -->

---

## Part 2: Reading a directory

### 3. Listing files and folders

- [ ] Use `os.listdir()` for the current directory.
- [ ] Use `os.listdir(path)` for a specific directory.
- [ ] Loop over the returned names.
- [ ] Understand that `os.listdir()` returns names, not complete paths.
- [ ] Build a complete path with `os.path.join()`.

**Try it:**

- [ ] List all entries in a practice folder.
- [ ] Print each entry on its own line.
- [ ] Find only the entries with a `.csv` extension.

**My notes:**

<!-- Add your explanation here. -->

### 4. Checking whether something exists

- [ ] Use `os.path.exists(path)`.
- [ ] Write an `if/else` check for an optional file such as `config.json`.
- [ ] Understand that a path can exist as either a file or a directory.

**My notes:**

<!-- Add your explanation here. -->

### 5. Distinguishing files and directories

- [ ] Use `os.path.isfile(path)`.
- [ ] Use `os.path.isdir(path)`.
- [ ] Classify every entry returned by `os.listdir()`.
- [ ] Understand why checking the type before an operation prevents errors.

**My notes:**

<!-- Add your explanation here. -->

---

## Part 3: Creating and removing directories

### 6. Creating one directory with `os.mkdir()`

- [ ] Create one new directory with `os.mkdir(path)`.
- [ ] Understand that it raises `FileExistsError` if the directory already
  exists.
- [ ] Check for existence before creating a directory when appropriate.

**My notes:**

<!-- Add your explanation here. -->

### 7. Creating nested directories with `os.makedirs()`

- [ ] Create multiple levels with `os.makedirs(path)`.
- [ ] Use `exist_ok=True` when an existing directory is acceptable.
- [ ] Explain the difference between `os.mkdir()` and `os.makedirs()`.

**Practice tree:**

```text
data/
└── reports/
    └── 2026/
```

- [ ] Create the practice tree.
- [ ] Confirm each level with `os.path.isdir()`.

### 8. Removing an empty directory

- [ ] Use `os.rmdir(path)` for an empty directory.
- [ ] Understand why `os.rmdir()` fails when the directory contains files.
- [ ] Remove child directories before their parent directory.

**My notes:**

<!-- Add your explanation here. -->

### 9. Removing a directory recursively

- [ ] Explain what `shutil.rmtree(path)` does.
- [ ] Understand that it removes the directory and all of its contents.
- [ ] Never run it on a path you have not checked carefully.
- [ ] Practice only inside a temporary test directory.

> **Safety rule:** Recursive deletion is powerful and irreversible. Prefer
> `os.rmdir()` for empty directories and validate every destructive path.

---

## Part 4: Managing files

### 10. Removing a file

- [ ] Use `os.remove(path)`.
- [ ] Check `os.path.exists(path)` before removal when the file is optional.
- [ ] Understand the difference between removing a file and removing a
  directory.

**My notes:**

<!-- Add your explanation here. -->

### 11. Renaming a file or directory

- [ ] Use `os.rename(old_path, new_path)`.
- [ ] Understand that renaming can also move an item when the destination
  directory is different.
- [ ] Check that the source exists before renaming.

**My notes:**

<!-- Add your explanation here. -->

### 12. Reading file size

- [ ] Use `os.path.getsize(path)`.
- [ ] Understand that the result is measured in bytes.
- [ ] Convert bytes to KB, MB, or GB.
- [ ] Explain why a missing path causes an error.

**Conversion notes:**

```text
KB = bytes / 1024
MB = bytes / (1024 * 1024)
GB = bytes / (1024 * 1024 * 1024)
```

---

## Part 5: Understanding file names and paths

### 13. Splitting a file extension

- [ ] Use `os.path.splitext(filename)`.
- [ ] Separate the file name from its extension.
- [ ] Filter files such as `.txt`, `.csv`, and `.pdf`.
- [ ] Compare extensions consistently, for example with `.lower()`.

**My notes:**

<!-- Add your explanation here. -->

### 14. Reading the file name from a path

- [ ] Use `os.path.basename(path)`.
- [ ] Explain why the basename is useful when displaying a file to a user.

### 15. Reading the parent directory from a path

- [ ] Use `os.path.dirname(path)`.
- [ ] Explain how it identifies the directory containing the item.

### 16. Joining paths safely

- [ ] Use `os.path.join("data", "users.csv")`.
- [ ] Understand why string concatenation such as `"data/" + "users.csv"` is
  less portable.
- [ ] Know that path separators differ between operating systems.

**My notes:**

<!-- Add your explanation here. -->

### 17. Relative and absolute paths

- [ ] Define a relative path.
- [ ] Define an absolute path.
- [ ] Use `os.path.abspath(path)` to create an absolute path.
- [ ] Explain when each kind of path is useful.

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
| Current location | Not started | |
| Reading directories | Not started | |
| Creating/removing directories | Not started | |
| Managing files | Not started | |
| File names and paths | Not started | |
| Next topics | Not started | |

### Questions to answer before moving on

- [ ] What is the difference between a file path and a file object?
- [ ] Why should paths be joined instead of concatenated?
- [ ] Why can `os.rmdir()` remove only empty directories?
- [ ] What makes `shutil.rmtree()` dangerous?
- [ ] How would you process every CSV file inside a folder safely?
