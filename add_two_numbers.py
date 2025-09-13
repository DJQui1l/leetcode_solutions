# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        

        # initialize two empty lists for list node values
        l1List = []
        l2List = []

        # appends l1 node values to l1List
        current_node = l1
        while current_node != None:
            l1List.append(current_node.val)
            current_node = current_node.next
        
         # appends l2 node values to l2List
        current_node = l2
        while current_node != None:
            l2List.append(current_node.val)
            current_node = current_node.next

        # reverse the lists
        l1List = l1List[::-1]
        l2List = l2List[::-1]

        # turn those lists into full numbers
        l1_num = int(''.join(str(x) for x in l1List))
        l2_num = int(''.join(str(x) for x in l2List))

        #get their sum
        outcome = l1_num + l2_num

        #split those numbers and add them to a list
        outcome_num_list = [int(char) for char in str(outcome)][::-1]

        # start off linked list with the first value in the outcome list
        outcomeNode = ListNode(outcome_num_list[0])

        #place that node in another variable for reference
        current = outcomeNode
        
        # for the rest of the values in the outcome list...
        for num in outcome_num_list[1:]:

            #create another listNode with a value and make that the next node
            current.next = ListNode(num)
            # set the current node to be the next node
            current = current.next

        
        return outcomeNode

