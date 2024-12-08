import re
import random
from functools import lru_cache

import nltk
from nltk.stem import WordNetLemmatizer


@lru_cache(maxsize=1024)
def preprocess_text(context: str) -> str:
    # https://mkjjo.github.io/python/2019/07/09/english_preprocessing.html
    return re.sub(r'[^\.\?\!\w\d\s]','', context).lower().replace('.','')


def unique_word_tokens(word_tokens: list) -> list:
    lemmatizer = WordNetLemmatizer()

    lemmatized_forms = {}
    unique_words = []

    for token in word_tokens:
        lemma = lemmatizer.lemmatize(token.lower(), 'v')

        if lemma not in lemmatized_forms:
            lemmatized_forms[lemma] = token
            unique_words.append(token)

    return unique_words


def blank_keyword(context: str, blank_count: int) -> dict:
    preprocessed_text = preprocess_text(context)  # 형태소 분석용 정제된 키워드

    question_token = nltk.word_tokenize(preprocessed_text)
    tagged_tokens = nltk.pos_tag(question_token)

    verb_tokens = [word for word, pos in tagged_tokens if pos.startswith('VB')]
    unique_tokens = unique_word_tokens(verb_tokens)

    # 본문에 없는 단어 제거
    for verb_token in unique_tokens:
        if verb_token not in context:
            unique_tokens.remove(verb_token)

    # Ensure blank_count doesn't exceed available verbs
    blankable_verbs = min(len(unique_tokens), blank_count)

    # Select verbs sequentially up to blank_count
    variation_keyword_list = unique_tokens[:blankable_verbs]

    # Replace verbs in the order they appear in the text
    question_variation = context
    for vr_keyword in variation_keyword_list:
        question_variation = question_variation.replace(vr_keyword, '_____ ', 1)

    return {"question": question_variation, "answer": variation_keyword_list}


def remove_unnecessary_quotes(text):
    pattern = r"""
            (?<!\w)'([\w,:;.!?'-]+)'(?!\w)  # Single-quoted words or words with punctuation
            |                              # OR
            (?<!\w)"([\w,:;.!?'-]+)"(?!\w)  # Double-quoted words or words with punctuation
        """

    cleaned_text = re.sub(pattern, lambda m: m.group(1) or m.group(2), text, flags=re.VERBOSE)
    return cleaned_text


# 해석 해야 하는데..
def blank_sentence(context: str, is_hint_all: bool = True) -> dict:
    sentences = re.split('[.?!]', context.strip())
    sentences.pop()  # 마지막 원소는 ''이기 때문에 제거해야 함
    choiced_sentence = random.choice(sentences).strip()

    if is_hint_all:
        shuffled_words = choiced_sentence.split(' ')
        random.shuffle(shuffled_words)

        hint_str = remove_unnecessary_quotes(str(tuple(shuffled_words)).replace(', ', ' / '))

        return {
                    "question": context.replace(choiced_sentence, '__________(?)__________'),
                    "hint": hint_str,
                    "answer": choiced_sentence
                }

    preprocessed_text = preprocess_text(context)  # 형태소 분석용 정제된 키워드

    question_token = nltk.word_tokenize(preprocessed_text)
    tagged_tokens = nltk.pos_tag(question_token)

    verb_tokens = [word for word, pos in tagged_tokens if pos.startswith('VB')]

    hint_str = str(tuple(verb_tokens)).replace(', ', ' / ')

    return {
        "question": context.replace(choiced_sentence, '__________(?)__________'),
        "hint": hint_str,
        "answer": choiced_sentence
    }