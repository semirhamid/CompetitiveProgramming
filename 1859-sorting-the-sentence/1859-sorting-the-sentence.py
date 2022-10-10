class Solution:
    def sortSentence(self, s: str) -> str:
        words_array = s.split()
        length = len(words_array)
        result_holder = [""] * length
        for word in words_array:
            index = int(word[-1]) - 1
            result_holder[index] = word[0:len(word)-1]
        sentence = " ".join(result_holder)
        return sentence