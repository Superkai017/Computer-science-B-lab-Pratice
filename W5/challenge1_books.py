import math


def push(stack, book):
    stack.append(book)


def pop(stack):
    if len(stack) == 0:
        return None
    return stack.pop()


def display(stack):
    index = len(stack) - 1
    while index >= 0:
        print(stack[index])
        index = index - 1


stack = []

book_a = {"book_no": 1, "book_name": "A", "price": 10}
book_b = {"book_no": 2, "book_name": "B", "price": 12}

push(stack, book_a)
push(stack, book_b)
display(stack)
display(stack)
print(stack)
print(pop(stack))
print(pop(stack))
print(pop(stack))

while True:
    command = input("Command (push, pop, display, exit): ")
    if command == "exit":
        break
    if command == "push":
        book_no_text = input("book_no: ")
        try:
            book_no = int(book_no_text)
        except ValueError:
            print("Invalid book number.")
            continue
        book_name = input("book_name: ").strip()
        if book_name == "":
            print("Invalid title.")
            continue
        price_text = input("price: ")
        try:
            price = float(price_text)
        except ValueError:
            print("Invalid price.")
            continue
        if not math.isfinite(price) or price < 0:
            print("Invalid price.")
            continue
        push(stack, {
            "book_no": book_no,
            "book_name": book_name,
            "price": price,
        })
        continue
    if command == "pop":
        print(pop(stack))
        continue
    if command == "display":
        display(stack)
        continue
    print("Invalid command.")
