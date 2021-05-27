# Generate Binary Numbers using Queue
# Between 1 to n
from collections import deque

def generate(n):
    #create an empty queue and enque 1
    q = deque()
    q.append('1')
    # run 'n' times
    for i in range(n):
        #remove the front element
        front = str(q.popleft())
        # append 0 and 1 to the front element
        #enque both strings
        q.append(front + '0')
        q.append(front + '1')
        # print the front element
        print(front, end = ' ')
if __name__ == '__main__':
    n = 16
    generate(n)