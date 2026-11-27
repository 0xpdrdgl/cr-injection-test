def reverse_words(sentence: str) -> str:
    return " ".join(word[::-1] for word in sentence.split(" "))


def count_vowels(text: str) -> int:
    return sum(1 for c in text.lower() if c in "aeiou")
