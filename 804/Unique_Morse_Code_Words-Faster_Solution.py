import string
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count=0

        def morseCodify(words):
            trasf=[]
            dictionary = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
            for word in words:
                codifiedWord=""
                for letter in word:
                    codifiedLetter=dictionary[letter]
                    codifiedWord = codifiedWord + codifiedLetter
                trasf.append(codifiedWord)
            return trasf
        trasf = morseCodify(words)
        trasf2=trasf
        for x, y in enumerate(set(trasf) & set(trasf2)):
            count+=1
        return count
