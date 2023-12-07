import os
import sys
from glob import glob


def rename_folders_and_files():
    # Получаем путь к исполняемому файлу
    executable_path = sys.executable

    # Получаем путь к директории, в которой находится исполняемый файл
    current_directory = os.path.dirname(executable_path)
    # Получаем текущую рабочую директорию (где находится скрипт)
    # current_directory = os.path.dirname(os.path.abspath(__file__))

    for folder in os.listdir(current_directory):
        folder_path = os.path.join(current_directory, folder)

        if os.path.isdir(folder_path):
            # Получаем название вложенной папки
            subfolder_name = os.path.join(folder_path, os.listdir(folder_path)[0])

            # Используем glob для поиска pdf файла внутри папки
            pdf_files = glob(os.path.join(folder_path, "*.pdf"))

            if pdf_files:
                # Получаем путь к pdf файлу
                pdf_file_path = pdf_files[0]

                # Получаем абсолютные пути для переименования
                new_subfolder_path = os.path.join(folder_path, folder)
                new_pdf_file_path = os.path.join(folder_path, f"{folder}.pdf")

                # Переименовываем папку
                os.rename(subfolder_name, new_subfolder_path)

                # Переименовываем pdf файл
                os.rename(pdf_file_path, new_pdf_file_path)


rename_folders_and_files()

# import os

# # Указываем путь к создаваемой папке (можно указать абсолютный или относительный путь)
# folder_path = "example"

# # Проверяем, существует ли папка с указанным именем
# if not os.path.exists(folder_path):
#     # Создаем папку
#     os.makedirs(folder_path)
#     print(f'Папка "{folder_path}" успешно создана.')
# else:
#     print(f'Папка "{folder_path}" уже существует.')
