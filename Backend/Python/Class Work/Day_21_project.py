class student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self._marks={}

    def add_mark(self,subject,mark):
        if mark >= 0 and mark <=100:
            self._marks[subject] = mark
        else:
            print('Invalid mark for', subject)
                 
    def calculate_total(self):
        total=0
        for subject in self._marks:
            total += self._marks[subject]
            global total
        return total
    
    def calculate_average(self):
        count=0
        for i in self._marks:
            count+=1
        if count == 0:
            return 0
        
        return total/count
        
    
ria=student('ria',12,67)
print(ria.add_mark('maths',10))
print(ria.calculate_average())