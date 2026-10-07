class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaSet = []
        for string in s.split():
            if not string.isalnum():
                word = string
                splitWord = []
                
                for letter in word:
                    
                    if letter.isalnum():
                       
                        splitWord.append(letter)
                word = "".join(splitWord)
            else:
                word = string
            alphaSet.append(word)
        s_string = "".join(alphaSet).casefold()
        return s_string == s_string[::-1]

        
                

            
                    
        print(alphaSet)
    
        return alphaSet == alphaSet[::-1]

            
        