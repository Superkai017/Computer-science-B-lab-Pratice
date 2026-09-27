def push_qualified(students, stack):
    for student, score in students.items():
        if score >= 75:
            stack.append(student)


def pop_all(stack):
    popped_names = []
    while stack:
        popped_names.append(stack.pop())
    return popped_names


stack = []
students = {
    "Vanna": 90,
    "Tena": 70,
    "Devi": 75,
    "Mina": 74,
    "Sok": 100,
}
push_qualified(students, stack)
print("Stack before popping:", stack)
print("Returned names:", pop_all(stack))
print("Stack after popping:", stack)
print()

# Boundary test: 74, 75, 76
boundary_stack = []
push_qualified({"A": 74, "B": 75, "C": 76}, boundary_stack)
print("74/75/76 qualified:", boundary_stack)

# Empty dictionary
empty_stack = []
push_qualified({}, empty_stack)
print("empty dict:", empty_stack)
print("pop_all on empty stack:", pop_all(empty_stack))

# Nobody qualifies
nobody_stack = []
push_qualified({"A": 10, "B": 74}, nobody_stack)
print("nobody qualifies:", nobody_stack)

# Everybody qualifies
everybody_stack = []
push_qualified({"A": 75, "B": 80, "C": 100}, everybody_stack)
print("everybody qualifies:", everybody_stack)

# Reused key: the second value replaces the first
reused = {"Vanna": 50, "Vanna": 90}
print("reused key dict:", reused)

"""
- Why is 75 an important test?: 
75 is important because it checks whether the boundary value is included
(a mistake like > instead of >= would only show up with exactly 75).

What happens when a dictionary key is reused?

Dictionary keys must be unique. If a key is reused, its old value is replaced by the new value;
it does not create a second entry."""
