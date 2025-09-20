class Solution:
    def isPalindrome(self, x: int) -> bool:

        #turn x 'int' into 'str'
        num_str = str(x)

        # get length of string
        num_str_len = len(num_str)

        # with that length, use string slicing to get the string in reverse starting at the last character and moving backwards.
        reverse_num_str = num_str[num_str_len-1::-1] # str[start:stop:step]
        if num_str == reverse_num_str:
            return True
        else:
            return False
        



        # print(num_str[num_str_len-1])
        # print(num_str[:num_str_len:-1])

        # if num_str == num_str[:num_str_len:-1]:
        #     return True
        # else:
        #     return False

        # if num_str[:num_str_len]:
        #     if num_str_len % 2 != 0:
        #         divider_index =int(((num_str_len - 1)/2))

        #         before = num_str[:divider_index]
        #         after = num_str[:divider_index:-1]
        #         print('odd,',before)
        #         print('odd,',after)
        #         if before == after:
        #             return True
        #         elif "-" in before:
        #             return False
        #         else:
        #             return False
            
        #     elif num_str_len % 2 == 0:
        #         half = int(num_str_len / 2)
        #         before = num_str[:half-1]
        #         after = num_str[:half-1:-1]

        #         print(before)
        #         print(after)

        #         if len(num_str) == 2 and num_str[0] == num_str[1]:
        #             return True
        #         if before == after:
        #             return True

        #         elif "-" in before:
        #             return False

        #         else:
        #             return False

        # else:
        #     return False

            
            
