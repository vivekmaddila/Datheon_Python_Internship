
import os
import shutil
import logging
from pathlib import Path

# Logging configuration
BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "organizer.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File extension mapping
FILE_TYPES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
    ".java": "Code"
}


def get_unique_path(destination):
    """Generate a unique filename if a file already exists."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):

    folder_path = Path(folder_path)

    moved = 0
    skipped = 0
    failed = 0

    category_counts = {}

    print("\n====================================")
    print("       AUTOMATED FILE ORGANIZER")
    print("====================================")

    if not folder_path.exists() or not folder_path.is_dir():
        print("Error: Invalid directory path.")
        logging.error("Invalid directory: %s", folder_path)
        return

    try:
        with os.scandir(folder_path) as entries:

            for entry in entries:

                if not entry.is_file():
                    continue

                source = Path(entry.path)

                category = FILE_TYPES.get(
                    source.suffix.lower()
                )

                if category is None:
                    print(f"Skipped: {source.name}")
                    skipped += 1
                    logging.info("Skipped: %s", source.name)
                    continue

                destination_folder = folder_path / category

                try:
                    destination_folder.mkdir(
                        parents=True,
                        exist_ok=True
                    )

                    destination = get_unique_path(
                        destination_folder / source.name
                    )

                    shutil.move(
                        str(source),
                        str(destination)
                    )

                    print(
                        f"Moved: {source.name} -> {category}"
                    )

                    moved += 1
                    category_counts[category] = (
                        category_counts.get(category, 0) + 1
                    )

                    logging.info(
                        "Moved %s to %s",
                        source.name,
                        category
                    )

                except FileExistsError:
                    print(f"File already exists: {source.name}")
                    failed += 1
                    logging.warning(
                        "File collision: %s", source.name
                    )

                except PermissionError:
                    print(f"Permission denied: {source.name}")
                    failed += 1
                    logging.error(
                        "Permission denied: %s", source.name
                    )

                except OSError as error:
                    print(f"Unable to move {source.name}: {error}")
                    failed += 1
                    logging.error(
                        "Move failed for %s: %s",
                        source.name,
                        error
                    )

    except PermissionError:
        print("Permission denied while accessing directory.")
        logging.error("Cannot access directory: %s", folder_path)
        return

    except OSError as error:
        print("Directory error:", error)
        logging.error("Directory error: %s", error)
        return

    print("\n====================================")
    print("          EXECUTION SUMMARY")
    print("====================================")

    print("Files moved   :", moved)
    print("Files skipped :", skipped)
    print("Files failed  :", failed)

    print("\nCategory-wise Summary:")

    for category, count in category_counts.items():
        print(f"{category}: {count} files")

    print("\nLog file:", LOG_FILE.name)
    print("File organization completed!")
    print("====================================")

    logging.info(
        "Completed. Moved=%d, Skipped=%d, Failed=%d",
        moved, skipped, failed
    )


if __name__ == "__main__":

    print("\nAUTOMATED FILE ORGANIZER")
    print("------------------------")

    folder = input(
        "Enter folder path to organize: "
    ).strip().strip('"')

    organize_files(folder)
