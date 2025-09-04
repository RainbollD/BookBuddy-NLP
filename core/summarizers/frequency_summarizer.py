import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

from nltk_data.downloader import download_nltk


class SimpleFrequencySummarizer:
    """
    Класс для поиска предложений с наибольшим количеством часто встречаемых слов.
    """

    def __init__(self, amount_sentence: int = 2):
        """
        Определяет количество предложений на выходе, загружает необходимые данные из nltk
        :param amount_sentence: Количество предложений в сокращенном варианте.
        """
        self.amount_sentence = amount_sentence

        nltk_path = download_nltk("stopwords")
        nltk.data.path.append(nltk_path)

    def summarize(self, text: str) -> str:
        """
        Выделяет предложения, которые содержат наибольшую частоту встречаемости слов в тексте.
        :param text: Текст, который необходимо сократить.
        :return:
        """
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())
        stop_words = stopwords.words('russian')
        filtered_words = [word for word in words if word not in stop_words and word.isalpha()]

        frequency = FreqDist(filtered_words)
        sentences_score = list(
            enumerate(sum(frequency[word] for word in word_tokenize(sentence.lower()) if word in filtered_words)
                      for sentence in sentences))

        sentences_score.sort(key=lambda x: x[1], reverse=True)

        summarized_sentence = sentences_score[:self.amount_sentence]
        summarized_sentence.sort(key=lambda x: x[0], reverse=False)

        summarized_text = []
        for idx, _ in summarized_sentence:
            summarized_text.append(sentences[idx])

        return '\n'.join(summarized_text)
