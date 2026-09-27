import heapq


class EmergencyRoom:
    def __init__(self):
        self.patients = []
        self.waiting_ids = set()
        self.arrival_number = 0

    def add_patient(self, name, severity, dob, id_number, gender):
        if not isinstance(name, str) or name.strip() == "":
            return False
        if not isinstance(id_number, str) or id_number.strip() == "":
            return False
        id_number = id_number.strip()

        if isinstance(severity, bool) or not isinstance(severity, int):
            return False
        if severity < 1 or severity > 5:
            return False
        if gender != "M" and gender != "F" and gender != "Other":
            return False
        if id_number in self.waiting_ids:
            return False
        self.arrival_number = self.arrival_number + 1
        patient = {
            "name": name,
            "severity": severity,
            "dob": dob,
            "id_number": id_number,
            "gender": gender,
        }
        heapq.heappush(self.patients, (severity, self.arrival_number, patient))
        self.waiting_ids.add(id_number)
        return True

    def treat_patient(self):
        if len(self.patients) == 0:
            return None
        entry = heapq.heappop(self.patients)
        patient = entry[2]
        self.waiting_ids.remove(patient["id_number"])
        return patient

    def show_next_patient(self):
        if len(self.patients) == 0:
            return None
        return self.patients[0][2]


room = EmergencyRoom()
print("Add Zara:", room.add_patient("Zara", 2, "1999-03-01", "Z1", "F"))
print("Add Ben:", room.add_patient("Ben", 1, "1998-05-02", "B1", "M"))
print("Add Amy:", room.add_patient("Amy", 1, "2001-07-03", "A1", "F"))


print("Peek 1:", room.show_next_patient())
print("Peek 2:", room.show_next_patient())
print("Patients still waiting:", len(room.patients))

print("Treat 1:", room.treat_patient())
print("Treat 2:", room.treat_patient())
print("Treat 3:", room.treat_patient())
print()

empty = EmergencyRoom()
print("Empty treat:", empty.treat_patient())
print("Empty peek:", empty.show_next_patient())
print()

duplicate = EmergencyRoom()
print("Add B1:", duplicate.add_patient("Kira", 1, "1998-05-02", "B1", "M"))
print("Add B1 again (new DOB):", duplicate.add_patient("Bothy", 1, "2002-01-01", "B1", "M"))
print("Next patient:", duplicate.show_next_patient())
print("Patients waiting:", len(duplicate.patients))
print()

shared = EmergencyRoom()
print("Add S1:", shared.add_patient("Sing", 3, "2000-01-01", "S1", "F"))
print("Add S2 (same DOB):", shared.add_patient("Tou", 4, "2000-01-01", "S2", "M"))
print("Patients waiting:", len(shared.patients))
print()

again = EmergencyRoom()
print("Add B1:", again.add_patient("Vid", 1, "1998-05-02", "B1", "M"))
print("Treat:", again.treat_patient())
print("Add B1 again after treatment:", again.add_patient("Vid", 1, "1998-05-02", "B1", "M"))
print()


invalid = EmergencyRoom()
print("Severity 0:", invalid.add_patient("Test", 0, "2000-01-01", "T1", "M"))
print("Severity 6:", invalid.add_patient("Test", 6, "2000-01-01", "T1", "M"))
print("Severity hello:", invalid.add_patient("Test", "hello", "2000-01-01", "T1", "M"))
print("Patients waiting:", len(invalid.patients))
print()



menu = EmergencyRoom()
while True:
    command = input("Command (add, treat, peek, exit): ")
    if command == "exit":
        break
    if command == "add":
        name = input("name: ")
        severity_text = input("severity (1-5): ")
        try:
            severity = int(severity_text)
        except ValueError:
            # keep the text; add_patient will reject it because it is not an int
            severity = severity_text
        dob = input("dob (YYYY-MM-DD): ")
        id_number = input("id_number: ")
        gender = input("gender (M, F, Other): ")
        if menu.add_patient(name, severity, dob, id_number, gender):
            print("Patient added.")
        else:
            print("Rejected: check severity 1-5, non-empty name and ID, gender, or duplicate waiting ID.")
        continue
    if command == "treat":
        print(menu.treat_patient())
        continue
    if command == "peek":
        print(menu.show_next_patient())
        continue
    print("Invalid command.")
    # Summary:
# - Heap entry = (severity, arrival_number, patient) -> lowest severity first.
# - Same severity -> lower arrival_number first (first come, first served).
# - Peek reads patients[0] only, so nothing is removed.
# - Empty queue -> treat and peek return None.
# - Duplicate waiting ID -> rejected, even with a different DOB.
# - Same DOB, different ID -> allowed.
# - Treated ID is removed from waiting_ids, so it can be added again.
# - Severity 0, 6, "hello" -> rejected (must be an int from 1 to 5).
# - Name tie-breaker -> "Amy" < "Ben" alphabetically, so Amy goes before Ben (wrong).

