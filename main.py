from queue import LifoQueue

## creating LifoQueue object
stack = LifoQueue()

## checking whether stack is empty or not -> true
print(stack.empty())

## pushing the elements
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)

## again checking whether stack is empty or not -> false
print(stack.empty())

## popping all the elements
print(stack.get())
print(stack.get())
print(stack.get())

## checking the stack size
print("Size", stack.qsize())

print(stack.get())
print(stack.get())

## checking the whether stack is empty or not for the last time -> true
print(stack.empty())