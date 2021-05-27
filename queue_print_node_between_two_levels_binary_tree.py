# Print Node between two levels in Binary Tree
# using Queues
from collections import deque
class Node:
    def __init__(self, key=None, left=None,
                 right=None):
        self.key = key
        self.left = left
        self.right = right
        
# Iterate function to print all nodes
# Between two levels
def printNodes(root, start, end):
    if root is None:
        return
    # Create an empty queue and enque root
    queue = deque()
    queue.append(root)
    #maintain the level of current node
    level = 0
    # Loop till queue is empty
    while queue:
        #increment level by 1
        level = level + 1
        size = len(queue)
        
        #process every node and enque non-empty
        # left and right child
        while size > 0:
            size = size - 1
            curr = queue.popleft()
            #print the node if its level
            # is between given levels
            if start <= level <= end:
                print(curr.key, end=' ')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if start <= level <= end:
            print()
            
if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    root.right.right.right = Node(30)
    
    start = 2
    end = 3
    printNodes(root, start, end)