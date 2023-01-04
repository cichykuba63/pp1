# defining a queue
queue = []

# adding value to the queue
def push(value):
    queue.append(value)

# poping item from the queue
def pop():
    return queue.pop(0)

# displaying a queue
def display():
    for element in queue:
        print(element)

# return True if queue is empty
def empty():
    return len(queue) == 0