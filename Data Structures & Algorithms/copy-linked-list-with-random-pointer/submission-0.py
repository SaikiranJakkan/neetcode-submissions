"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Pre-loaded with None:None (the clever part, explained below)
        oldToCopy = { None : None }

        # ── PASS 1: create a copy of every node ──
        cur = head
        while cur:
            copy = Node(cur.val)      # make a copy (just the value)
            oldToCopy[cur] = copy     # map original → copy
            cur = cur.next            # move forward
        # After this: all copies exist, but none are linked yet

        # ── PASS 2: connect the copies ──
        cur = head
        while cur:
            copy = oldToCopy[cur]                  # grab this node's copy
            copy.next   = oldToCopy[cur.next]      # link copy's next
            copy.random = oldToCopy[cur.random]    # link copy's random
            cur = cur.next

        # Return the copy of the original head
        return oldToCopy[head]
        