class Solution:
    def romanToInt(self, s: str) -> int:
        
        #hard coded roman_numerals
        roman_numerals = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000,
            
            }

        # start count
        count = 0
        
        """
        If you find any grouped numerals, 
        remove them from string and add what they're worth
        to the count. 
        """
        if 'IV' in s:
            s = s.replace('IV','')
            count += roman_numerals['IV']
            
        if 'IX' in s:
            s = s.replace('IX','')
            count += roman_numerals['IX']

        if 'XL' in s:
            s = s.replace('XL','')
            count += roman_numerals['XL']

        if 'XC' in s:
            s = s.replace('XC','')
            count += roman_numerals['XC']

        if 'CD' in s:
            s = s.replace('CD','')
            count += roman_numerals['CD']

        if 'CM' in s:
            s = s.replace('CM','')
            count += roman_numerals['CM']

        """
        With all the grouped numerals removed,
        add the single numeral values.
        
        """
        for char in s:
            count += roman_numerals[char]

        return count