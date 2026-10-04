"""Interactive, safe lessons for Python's built-in ``os`` module.

Run ``python os_tut.py`` for the menu, or ``python os_tut.py --lesson all``
to run the complete walkthrough.
"""

from __future__ import annotations

import argparse
import os
import platform
import shutil
import tempfile
from pathlib import Path
from typing import Callable


Lesson = Callable[[], None]


def heading(title: str) -> None:
    """Print a consistent lesson heading."""
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def show_path_concepts() -> None:
    """Explain current, relative, absolute, and joined paths."""
    heading("1. Paths and the current working directory")
    current = os.getcwd()
    relative = os.path.join("data", "notes.txt")
    absolute = os.path.abspath(relative)

    print(f"Current directory : {current}")
    print(f"Relative path    : {relative}")
    print(f"Absolute path    : {absolute}")
    print(f"Path separator    : {os.sep!r}")
    print(f"File name         : {os.path.basename(absolute)}")
    print(f"Parent directory  : {os.path.dirname(absolute)}")

    print("\nUse os.chdir(path) only when a program genuinely needs to change")
    print("process-wide state. Prefer absolute paths or pathlib.Path in larger apps.")


def show_directory_listing() -> None:
    """Create a temporary tree and demonstrate safe directory inspection."""
    heading("2. Listing files and directories")
    with tempfile.TemporaryDirectory(prefix="os-lesson-") as workspace:
        root = Path(workspace)
        (root / "documents").mkdir()
        (root / "documents" / "readme.txt").write_text("Welcome!\n", encoding="utf-8")
        (root / "images").mkdir()
        (root / "config.json").write_text('{"debug": true}\n', encoding="utf-8")

        print(f"Example workspace: {root}")
        print("os.listdir(root):")
        for name in sorted(os.listdir(root)):
            print(f"  - {name}")

        print("\nOnly files:")
        for name in sorted(os.listdir(root)):
            item = root / name
            if os.path.isfile(item):
                print(f"  - {item.name}")

        print("\nOnly directories:")
        for name in sorted(os.listdir(root)):
            item = root / name
            if os.path.isdir(item):
                print(f"  - {item.name}/")


def show_file_operations() -> None:
    """Demonstrate create, rename, inspect, and delete operations."""
    heading("3. Creating, inspecting, renaming, and deleting")
    with tempfile.TemporaryDirectory(prefix="os-lesson-") as workspace:
        root = Path(workspace)
        data_dir = root / "data"
        nested_dir = data_dir / "reports" / "2026"

        os.makedirs(nested_dir, exist_ok=True)
        source = data_dir / "draft.txt"
        source.write_text("A small example file.\n", encoding="utf-8")
        renamed = data_dir / "final.txt"

        print(f"Created nested directory: {nested_dir.relative_to(root)}")
        print(f"File exists? {os.path.exists(source)}")
        print(f"Is a file?    {os.path.isfile(source)}")
        print(f"Size (bytes):  {os.path.getsize(source)}")

        os.rename(source, renamed)
        print(f"Renamed to: {renamed.name}")

        os.remove(renamed)
        print(f"Removed file? {not os.path.exists(renamed)}")
        os.rmdir(nested_dir)
        os.rmdir(nested_dir.parent)
        print("Removed the now-empty report directories with os.rmdir().")

        print("\nSafety note: shutil.rmtree() recursively deletes a directory.")
        print("Use it only with a path you have validated; this lesson never needs it.")


def show_environment_and_system() -> None:
    """Read environment variables and basic platform information."""
    heading("4. Environment variables and system information")
    user = os.environ.get("USER") or os.environ.get("USERNAME", "unknown")
    print(f"Python executable : {os.sys.executable}")
    print(f"Operating system  : {platform.system()}")
    print(f"OS release        : {platform.release()}")
    print(f"Current user      : {user}")
    print(f"HOME directory    : {os.environ.get('HOME', 'not set')}")
    print("\nNever print or commit secrets such as API keys from os.environ.")


def show_file_filtering() -> None:
    """Filter a directory by extension, a common automation pattern."""
    heading("5. Filtering files by extension")
    with tempfile.TemporaryDirectory(prefix="os-lesson-") as workspace:
        root = Path(workspace)
        names = ("users.csv", "notes.txt", "report.csv", "photo.png")
        for name in names:
            (root / name).write_text("example\n", encoding="utf-8")

        print(f"CSV files in {root}:")
        for name in sorted(os.listdir(root)):
            stem, extension = os.path.splitext(name)
            if extension.lower() == ".csv":
                print(f"  - {name} (name: {stem}, extension: {extension})")


LESSONS: dict[str, tuple[str, Lesson]] = {
    "paths": ("Paths and the current working directory", show_path_concepts),
    "listing": ("Listing files and directories", show_directory_listing),
    "files": ("Creating and managing files", show_file_operations),
    "system": ("Environment and system information", show_environment_and_system),
    "filter": ("Filtering files by extension", show_file_filtering),
}


def run_lesson(lesson_name: str) -> None:
    """Run one lesson or every lesson in the recommended order."""
    if lesson_name == "all":
        for _, lesson in LESSONS.values():
            lesson()
        return

    try:
        LESSONS[lesson_name][1]()
    except KeyError as error:
        valid = ", ".join((*LESSONS, "all"))
        raise SystemExit(f"Unknown lesson {lesson_name!r}. Choose: {valid}") from error


def interactive_menu() -> None:
    """Let a learner choose lessons interactively."""
    while True:
        heading("Python OS Fundamentals")
        for number, (key, (title, _)) in enumerate(LESSONS.items(), start=1):
            print(f"{number}. {title} [{key}]")
        print("A. Run all lessons")
        print("Q. Quit")

        choice = input("\nChoose a lesson: ").strip().lower()
        if choice == "q":
            print("Happy learning!")
            return
        if choice == "a":
            run_lesson("all")
            input("\nPress Enter to return to the menu...")
            continue

        keys = list(LESSONS)
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            run_lesson(keys[int(choice) - 1])
            input("\nPress Enter to return to the menu...")
        else:
            print("Please choose a listed number, A, or Q.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lesson",
        choices=(*LESSONS, "all"),
        help="run one lesson without opening the interactive menu",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.lesson:
        run_lesson(args.lesson)
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
