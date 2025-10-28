class Student:
    def __init__(self, name, roll_number, marks=None):
        self.name = name
        self.roll_number = roll_number
        self._marks = {} if marks is None else marks

    def add_mark(self, subject, mark):
        if 0 <= mark <= 100:
            self._marks[subject] = mark
        else:
            print('Invalid mark for', subject)

    def calculate_total(self):
        total = 0
        for subject in self._marks:
            total += self._marks[subject]
        return total

    def calculate_average(self):
        if not self._marks:  
            return 0
        total = self.calculate_total()
        return total / len(self._marks)


ria = Student('Ria', 12, 67)
ria.add_mark('Maths', 10)
print("Average:", ria.calculate_average())
