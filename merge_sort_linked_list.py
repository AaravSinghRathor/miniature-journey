import sys


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.ptr = None

    def create_linked_list(self, val_list):

        for value in val_list:
            node = ListNode(value)
            if not self.head:
                self.head = node
                self.ptr = self.head
            else:
                self.ptr.next = node
                self.ptr = self.ptr.next

        return self.head

    @staticmethod
    def print_linked_list(linked_list_head):

        ptr = linked_list_head
        vals = []
        while ptr:
            vals.append(ptr.val)
            ptr = ptr.next

        return "->".join([str(i) for i in vals])


class Solution:

    @staticmethod
    def merge_sorted_linked_list(head_list_1, head_list_2):

        if not head_list_1 and not head_list_2:
            return

        if not head_list_1:
            return head_list_2

        if not head_list_2:
            return head_list_1

        ptr_list_1 = head_list_1
        ptr_list_2 = head_list_2

        ptr_merged_list = None
        head_merged_list = None

        if ptr_list_1.val < ptr_list_2.val:
            head_merged_list = ptr_list_1
            ptr_list_1 = ptr_list_1.next
        else:
            head_merged_list = ptr_list_2
            ptr_list_2 = ptr_list_2.next

        ptr_merged_list = head_merged_list

        while ptr_list_1 and ptr_list_2:

            if ptr_list_1.val < ptr_list_2.val:
                ptr_merged_list.next = ptr_list_1
                ptr_list_1 = ptr_list_1.next
            else:
                ptr_merged_list.next = ptr_list_2
                ptr_list_2 = ptr_list_2.next

            ptr_merged_list = ptr_merged_list.next

        if ptr_list_1:
            ptr_merged_list.next = ptr_list_1
        elif ptr_list_2:
            ptr_merged_list.next = ptr_list_2

        return head_merged_list

    @staticmethod
    def find_mid_linked_list(linked_list_head):

        if not linked_list_head:
            return

        slow_ptr = linked_list_head
        fast_ptr = linked_list_head.next

        while fast_ptr and fast_ptr.next:

            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr

    def merge_sort(self, linked_list_head):

        if not linked_list_head:
            return
        if not linked_list_head.next:
            return linked_list_head

        mid_element = self.find_mid_linked_list(linked_list_head)
        print(f"Mid element is {mid_element.val}")

        list_1_head = linked_list_head
        list_2_head = mid_element.next
        mid_element.next = None

        print(f"Linked list 1: {LinkedList().print_linked_list(list_1_head)}")
        print(f"Linked list 2: {LinkedList().print_linked_list(list_2_head)}")

        sorted_list_1_head = self.merge_sort(list_1_head)
        sorted_list_2_head = self.merge_sort(list_2_head)
        merged_sorted_list_head = self.merge_sorted_linked_list(sorted_list_1_head, sorted_list_2_head)

        return merged_sorted_list_head


# linked_list_1_nodes_val = [1, 2, 11]
# linked_list_2_nodes_val = [4, 5, 7, 10]
#
# linked_list_1 = LinkedList()
# head_linked_list_1 = linked_list_1.create_linked_list(linked_list_1_nodes_val)
#
# linked_list_2 = LinkedList()
# head_linked_list_2 = linked_list_2.create_linked_list(linked_list_2_nodes_val)
#
# merged_sorted_list_head = Solution().merge_sorted_linked_list(head_linked_list_1, head_linked_list_2)

linked_list_vals = []
linked_list_1 = LinkedList()
head_linked_list_1 = linked_list_1.create_linked_list(linked_list_vals)

sorted_linked_list_head = Solution().merge_sort(head_linked_list_1)

print(LinkedList().print_linked_list(sorted_linked_list_head))









