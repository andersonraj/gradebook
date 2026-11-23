import json
import os


class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            raise ValueError("Student already exists")
        self.students[name] = []

    def add_grade(self, name, grade):
        if name not in self.students:
            raise KeyError("Student not found")
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.students[name].append(grade)

    def average(self, name):
        if name not in self.students:
            raise KeyError("Student not found")
        grades = self.students[name]
        if len(grades) == 0:
            return 0
        total = 0
        for g in grades:
            total = total + g
        return total / len(grades)

    def letter_grade(self, name):
        avg = self.average(name)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def report(self, name):
        if name in self.students:
            if len(self.students[name]) > 0:
                avg = self.average(name)
                count = len(self.students[name])
                if avg >= 90:
                    status = "Excellent"
                else:
                    if avg >= 60:
                        status = "Passing"
                    else:
                        status = "At risk"
                return f"{name}: {avg:.1f} ({status})"
            else:
                return f"{name}: no grades"
        else:
            return "Student not found"

    def class_statistics(self):
        averages = []
        for name in self.students:
            if len(self.students[name]) > 0:
                averages.append(self.average(name))
        if len(averages) == 0:
            return {"highest": 0, "lowest": 0, "mean": 0}
        highest = averages[0]
        lowest = averages[0]
        for a in averages:
            if a > highest:
                highest = a
            if a < lowest:
                lowest = a
        return {
            "highest": highest,
            "lowest": lowest,
            "mean": sum(averages) / len(averages),
        }

    def load_from_file(self, path):
        try:
            with open(path) as f:
                self.students = json.load(f)
        except:
            self.students = {}