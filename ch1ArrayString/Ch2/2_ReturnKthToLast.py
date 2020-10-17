from LinkedList import SinglyLinkedList
import random
import math

def k2Last(ll, k):
    if ll.head is None:
        return None
    
    runner = current = ll.head
    for i in range(k):
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next
    
    return current

ll = SinglyLinkedList()
for i in range (0,9):
    elem = math.floor(9*random.random())
    ll.append(i)

k = math.floor(8*random.random())

print(ll)
print(str(k) + ": k index")
print(k2Last(ll,k))

