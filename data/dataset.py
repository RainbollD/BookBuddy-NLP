import os
import fitz


def exist_file(path: str):
    """Проверка на наличие файла """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл не найден. Путь {path}")


def load_pdf(data_path) -> str:
    """
    Загрузка текста из pdf файла
    :param data_path: Путь к pdf файлу.
    :return: Текст из файла.
    """
    doc = fitz.open(data_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    return text


def load_txt(data_path: str) -> str:
    """
    Загрузка текста из txt файла
    :param data_path: Путь к txt файлу.
    :return: Текст из файла.
    """
    with open(data_path, 'r') as file:
        return file.read()


def load_dataset(data_path: str):
    """
    Основная функция контроля загрузки данных с разными типами.
    :param data_path: Путь к файлу для чтения
    :return: Текст файла.
    """
    exist_file(data_path)

    data_type = data_path.rsplit('.', 1)[-1]

    if data_type == "pdf":
        text = load_pdf(data_path)
    elif data_type == "txt":
        text = load_txt(data_path)
    else:
        raise ValueError("Используется недопустимый тип данных\nСписок допустимых: str, pdf")

    return text


if __name__ == '__main__':
    path = "/home/lev/Downloads/Telegram Desktop/5AI.pdf"
    load_dataset(path)
