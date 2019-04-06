import string
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count=0

        def morseCodify(words):
            table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            word=""
            trasf=[]
            for i in words:
                for j in i:
                    for x, y in enumerate(string.ascii_lowercase, 0):
                        if j==y:
                            word = word + table[x]
                trasf.append(word)
                word=""
            return trasf
        trasf = morseCodify(words)
        trasf2=trasf
        for x, y in enumerate(set(trasf) & set(trasf2)):
            count+=1
        return count
