

#stack implementation in python

#creating an empty stack
def create_stack():
    stack=[]
    return stack
#check wheather the stack is empty
def is_empty(stack):
    return len(stack)==0

#insertion
def push(stack,item):
    stack.append(item)
    print("pushed item:" + item)

#deletion
def pop(stack):
    if is_empty(stack):
        return "stack is empty"
    return stack.pop()

#travesing
def travesing(stack):
    if is_empty(stack):
        print("Stack is empty")
    else:
        print("Traversing:")
        for item in reversed(stack):  # Traversing from top to bottom
            print(item)

stack=create_stack()
print("Inserting elements in the stack: \n")
push(stack , str(1))
push(stack , str(2))
push(stack , str(3))
push(stack , str(4))
push(stack , str(5))

print("stack after insertion:"+ str(stack),"\n")

print("popped item:"+ pop(stack))

print("stack after popping:"+ str(stack),"\n")

travesing(stack)

