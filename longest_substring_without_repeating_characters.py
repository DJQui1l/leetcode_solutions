class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        # I need to check for a unique set of character in order.
        # s = ""
        # if len(s) > 0:
        #     char_map = {}
        #     for char in s:
        #         char_map[char] = 0
            

        #     sub_string_list = []
        #     for char in s:
        #         if char in char_map:
                    
        #             char_map[char] += 1

                    
        #             if char_map[char] == 1:
        #                 sub_string_list.append(char)


        #     sub_string = ''.join(sub_string_list)
        #     print(char_map) 
        #     print(sub_string_list)
        #     # return len(sub_string)

        #     for i in range(len(sub_string_list)):
        #         # sub_string = ''.join(sub_string_list)
                
        #         if sub_string[i:] in s:
        #             print(sub_string[i:])
        #             return len(sub_string[i:])

        # else:
        #     return 0

        #idea is place a char, check if there's another char in that list
        # index = 0
        # char_list = []
        # hold = []
        # s_list = [char for char in s]
        # print(s_list)
        # while index <= len(s_list):
        #     if (s_list[index] in char_list) and (len(char_list) > 0):
        #         hold.append( char_list[char_list.index(s_list[index])])
        #     char_list.append(s[index])
            
        #     index +=1

        # print(char_list)
        s = "dvdf"
        s_list = [char for char in s]

        if len(s_list) < 1:
            return 0

        char_map = {}
        for char in s:
            char_map[char] = 0

        

        sub_string_list = []
        for i in range(len(s_list)):
            if s_list[i] in char_map:
                char_map[s_list[i]] += 1
                
                if char_map[s_list[i]] == 1:
                    sub_string_list.append(s_list[i])



        print(char_map) 
        print(sub_string_list)
        for i in range(len(sub_string_list)):
            substring = ''.join(sub_string_list)
            if substring[i:] in s:

                return len(substring[i:])
            

        # what if we have a counter that tracks the first instances of each character
        """ 
        like for "abcabcbb"
        a - 1 substring_count = 1
        b - 1 substring_count = 2
        c - 1 substring_count = 3
        a - 2 substring_count = 1 | since a was already found
        b - 1 substring_count = 2
        c - 1 substring_count = 3 
        b - 1 substring_count = 3 | since b wasn't the first found

        so substring_count would keep track of how many positions the substring takes within a string.
        and i'd need to have something else keep track of the index of the string where the substring starts so that
        I could return something like

        substring_count = 0
        for i in range(len(s_list)):
            
            do something
            
        return len(s[i:substring_count])

        """

        
        

        

        # return len(sub_string)
        

        # recurrence = 0
        # for key, value in char_map.items():
        #     if char_map[key] =

        
        