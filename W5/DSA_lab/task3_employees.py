class Node:
    def __init__(self, employee):
        self.employee = employee
        self.next = None


class EmployeeList:
    def __init__(self):
        self.head = None

    def add_employee(self, emp_no, name, salary, dept_no):

        if self.search_employee(emp_no) is not None:
            return False

        new_node = Node({
            'emp_no': emp_no,
            'name': name,
            'salary': salary,
            'dept_no': dept_no
        })

        if self.head is None:
            self.head = new_node
            return True

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return True

    def search_employee(self, emp_no):
        current = self.head
        while current is not None:
            if current.employee['emp_no'] == emp_no:
                return current.employee
            current = current.next
        return None

    def remove_employee(self, emp_no):
        current = self.head
        previous = None

        while current is not None:
            if current.employee['emp_no'] == emp_no:
                if previous is None:
                    # Removing the head node
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def all_employees(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.employee)
            current = current.next
        return result


# ---------- Part A: follow two nodes ----------
node101 = Node({'emp_no': 101, 'name': 'Vanna', 'salary': 50000, 'dept_no': 1})
node102 = Node({'emp_no': 102, 'name': 'Tena', 'salary': 60000, 'dept_no': 2})

node101.next = node102
head = node101

print("Part A")
print(head.employee['emp_no'])       # 101
print(head.next.employee['emp_no'])  # 102
print(head.next.next)                # None
print()


# Helper: build a fresh list with 101, 102, 103
def make_list():
    new_list = EmployeeList()
    new_list.add_employee(101, 'Vanna', 50000, 1)
    new_list.add_employee(102, 'Tena', 60000, 2)
    new_list.add_employee(103, 'Devi', 55000, 1)
    return new_list


# ---------- Part B: checks ----------
print("Part B")
emp_list = make_list()
print("All employees after adding 101, 102, 103:")
for emp in emp_list.all_employees():
    print(emp)

print("Search 102:", emp_list.search_employee(102))
print("Add 102 again:", emp_list.add_employee(102, 'Duplicate', 1000, 1))
print("Count after duplicate add:", len(emp_list.all_employees()))
print("Search 999:", emp_list.search_employee(999))
print("Remove 999:", emp_list.remove_employee(999))
print()

# Fresh list for each removal case
first_case = make_list()
print("Remove first (101):", first_case.remove_employee(101), first_case.all_employees())

middle_case = make_list()
print("Remove middle (102):", middle_case.remove_employee(102), middle_case.all_employees())

last_case = make_list()
print("Remove last (103):", last_case.remove_employee(103), last_case.all_employees())

# Remove the only node
single = EmployeeList()
single.add_employee(101, 'Vanna', 50000, 1)
print("Remove only node:", single.remove_employee(101), "head is None:", single.head is None)

# Empty list
empty = EmployeeList()
print("Empty all_employees:", empty.all_employees())
print("Empty search 101:", empty.search_employee(101))
print("Empty remove 101:", empty.remove_employee(101))
# Question 1: which link changes when you remove a middle node?
 #the previous node's next link changes. 
 # It skips the removed node and
 # points to the node after it.
#Question 2: how does search know it reached the end?
 #the search stops when current becomes None. The last node's next is None, 
 # so reaching None means there are no more nodes to check.