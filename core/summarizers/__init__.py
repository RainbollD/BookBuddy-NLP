"""
Инициализация алиасов и модулей для задачи сокращения текстов.
"""


from .frequency_summarizer import SimpleFrequencySummarizer
from .luhn_summarizer import LhuSummarizer
from .lexRank_summarizer import LexRankSummarizer
from .lsa_summaraizer import LsaSummarizer

__all__ = [
    "SimpleFrequencySummarizer",
    "LhuSummarizer",
    "LexRankSummarizer",
    "LsaSummarizer"
]
