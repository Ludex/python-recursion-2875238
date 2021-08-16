"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


class Node:
    def __init__(self, data, next=None):
        #Class constructor
        self.data = data
        self.next = next #next is a keyword in Python, so not advisable

def traverse(head):
    if head is None:
        return
    #recursive call
    print(head.data)
    traverse(head.next)

item1 = Node('dog')
item2 = Node('cat')
item3 = Node('rat')
item1.next = item2
item2.next = item3

#traverse(item1)

#Creating the linked list in one line of code
linked_list = Node('dog',Node('cat',Node('rat', None)))
traverse(linked_list)