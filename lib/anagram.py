class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        sorted_word = sorted(self.word.lower())
        
        for word in words:
            # Ignore identical words
            if word.lower() == self.word.lower():
                continue

            # Check if the sorted characters of the word match the sorted characters of self.word
            if sorted(word.lower()) == sorted_word:
                anagrams.append(word)

        return anagrams