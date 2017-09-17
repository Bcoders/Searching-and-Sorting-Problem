"""
Complete the function provided in the editor below.
It has one parameter: a pointer to a Node object named head that points
to the head of a linked list. Your function must return a boolean denoting
whether or not there is a cycle in the list. If there is a cycle,
return true; otherwise, return false."""

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    
    head1 = head #for short iteration
    head2 = head #for fast iteration
    while(True):
        
        
        head1 = head1.next
        head2 = head2.next
        if head2 != None:
            head2 = head2.next
        else:
            return False
        
        if (head1 == head2):
            return True
