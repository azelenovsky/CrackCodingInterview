from LinkedList import SinglyLinkedList 
from LinkedList import ListNode
import random
import math

def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next

ll = SinglyLinkedList()
ll.append('A')
ll.append('B')
MidNode = ListNode('C')
ll.append(MidNode)
ll.append('D')
ll.append('E')

print(ll)
delete_middle_node(MidNode)
print(ll)
