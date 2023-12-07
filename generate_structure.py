import os
import shutil


def generate_structure(base_folder, num_tomes, num_files):
    # Создаем основную папку X
    os.makedirs(base_folder, exist_ok=True)

    for i in range(1, num_tomes + 1):
        # Создаем папку с томом
        tome_folder = os.path.join(base_folder, f"Том{i}")
        os.makedirs(tome_folder, exist_ok=True)

        # Создаем папку to_rename внутри папки с томом
        to_rename_folder = os.path.join(tome_folder, "to_rename")
        os.makedirs(to_rename_folder, exist_ok=True)

        # Создаем несколько текстовых файлов в папке to_rename
        for j in range(1, num_files + 1):
            file_path = os.path.join(to_rename_folder, f"{chr(ord('a') + j - 1)}.txt")
            with open(file_path, "w") as file:
                file.write(f"Content of file {chr(ord('a') + j - 1)}")

        # Создаем файл index.pdf на уровне папки to_rename
        pdf_path = os.path.join(tome_folder, "index.pdf")
        with open(pdf_path, "w") as pdf_file:
            pdf_file.write("Content of index.pdf")


if __name__ == "__main__":
    # Укажите путь к основной папке, которую вы хотите создать
    base_folder_path = "x"

    # Укажите количество томов и количество файлов в каждой папке to_rename
    num_tomes = 5
    num_files = 5

    generate_structure(base_folder_path, num_tomes, num_files)
