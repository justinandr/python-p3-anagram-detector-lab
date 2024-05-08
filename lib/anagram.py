class Anagram:
    def __init__(self, word):
        self.word = sorted(word)

    def match(self, list):
        matches = []

        for word in list:
            if sorted(word) == self.word:
                matches.append(word)

        return matches
