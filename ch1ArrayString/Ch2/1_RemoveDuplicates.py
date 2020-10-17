from LinkedList import SinglyLinkedList
import random

def remove_dups(ll):
    if ll.head is None:
        return
    
    current = ll.head
    seen = set([current.data])
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
    
    return ll

def remove_dups_no_cache(ll):
    if ll.head is None:
        return
    
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    
    return ll.head

ll = SinglyLinkedList()
for i in range(0,99):
    ll.append(100*random.random())

print(ll)
remove_dups(ll)
print(ll)


ll = SinglyLinkedList()
for i in range(0,99):
    ll.append(100*random.random())

print(ll)
remove_dups_no_cache(ll)
print(ll)

ll = SinglyLinkedList()
ll.append('A')
ll.append('B')
ll.append('B')
print(ll)
remove_dups_no_cache(ll)
print(ll)