class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagrams = []

        for word in words:
            lowercase_word = word.lower()

            if sorted(lowercase_word) == sorted(self.word):
                anagrams.append(word)

        return anagrams