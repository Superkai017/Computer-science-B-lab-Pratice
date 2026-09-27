def push(stack, value):
    # add value to the top
    stack.append(value)

def pop(stack):
    # return the top number, or None if empty
    if is_empty(stack):
        return None
    return stack.pop()

def is_empty(stack):
    return len(stack) == 0


# Edge case: empty stack
empty_stack = []
print("empty pop:", pop(empty_stack))
print("empty is_empty? :", is_empty(empty_stack))

# Edge case: stack with one number
one_stack = [7]
print("one-number pop:", pop(one_stack))
print("after pop:", one_stack, "is_empty? :", is_empty(one_stack))
print()

# Main operations
stack = []

push(stack, 5)
print("after push 5:", stack)

push(stack, 10)
print("after push 10:", stack)

push(stack, 15)
print("after push 15:", stack)

popped = pop(stack)
print("popped:", popped)
print("after pop:", stack)

print("is_empty? :", is_empty(stack))

push(stack, 20)
print("after push 20:", stack)

# 15 leaves first because it was the last one added (LIFO: last in, first out).
# return gives the value back to the caller so it can be stored and used later;
# print only shows text on the screen and gives nothing back (the function returns None).
