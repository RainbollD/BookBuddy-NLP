import os
import nltk


def find_project_root(project_name: str = "BookBuddy-NLP"):
    path = str(os.path.abspath(__file__).split(project_name)[0])
    return path + project_name


def download_nltk(package_name: str):
    nltk_data_path = f"{find_project_root()}/nltk_data/{package_name}/"
    try:
        nltk.data.find(nltk_data_path)
    except LookupError:
        nltk.download("stopwords", download_dir=nltk_data_path)

    return nltk_data_path
