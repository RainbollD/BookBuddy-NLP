from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer as lexRank
from sumy.nlp.stemmers import Stemmer


class LexRankSummarizer:
    def __init__(self, amount_sentence: int = 2):
        self.amount_sentence = amount_sentence
        stemmer = Stemmer('russian')
        self.summarizer = lexRank(stemmer)

    def summarize(self, text: str) -> str:
        parser = PlaintextParser.from_string(text, Tokenizer("russian"))
        summary = self.summarizer(parser.document, self.amount_sentence)
        return "\n".join(map(str, summary))
