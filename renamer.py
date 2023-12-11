import sys
from pathlib import Path


def rename_folders_and_files() -> None:
    current_directory = (
        Path(sys.executable).parent
        if __name__ == "__main__"
        else Path(__file__).resolve().parent
    )

    for folder_path in current_directory.iterdir():
        if folder_path.is_dir():
            for sub_path in folder_path.iterdir():
                if sub_path.is_dir():
                    new_subfolder_path = folder_path / folder_path.name
                    sub_path.rename(new_subfolder_path)

                if sub_path.suffix.lower() == ".pdf" and sub_path.is_file():
                    new_pdf_file = folder_path / f"{folder_path.name}.pdf"
                    sub_path.rename(new_pdf_file)


if __name__ == "__main__":
    rename_folders_and_files()
