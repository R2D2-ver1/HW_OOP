class Student:
    students_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students_list.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade_s(self):
        sum = 0
        grade_s = []
        for c, gs in self.grades.items():
            for g in gs:
                sum += g
                grade_s.append(g)
        if len(grade_s) != 0:
            res = sum / len(grade_s)
            return round(res, 1)
        else:
            return 'Оценок еще нет'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._average_grade_s()}' \
              f'\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._average_grade_s() < other._average_grade_s()
        else:
            return

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def _average_grade_l(self):
        sum = 0
        grade_l = []
        for c, gs in self.grades.items():
            for g in gs:
                sum += g
                grade_l.append(g)
        if len(grade_l) != 0:
            res = sum / len(grade_l)
            return round(res, 1)
        else:
            return 'Оценок еще нет'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average_grade_l()}'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade_l() < other._average_grade_l()
        else:
            return

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res



Wanda = Student('Wanda', 'Maximoff', 'your_gender')
Wanda.courses_in_progress += ['Python']
Wanda.courses_in_progress += ['GIT']
Wanda.courses_in_progress += ['English for pro']
Wanda.add_courses("Введение в программирование")

Scott = Student('Scott', 'Lang', 'your_gender')
Scott.courses_in_progress += ['Python']
Scott.courses_in_progress += ['GIT']
Scott.courses_in_progress += ['Math. analysis']
Scott.add_courses("Введение в программирование")

Anthony = Lecturer('Anthony', 'Stark')
Anthony.courses_attached += ['Python']
Anthony.courses_attached += ['GIT']
Anthony.courses_attached += ['English for pro']

Stephen = Lecturer('Stephen', 'Strange')
Stephen.courses_attached += ['Python']
Stephen.courses_attached += ['GIT']
Stephen.courses_attached += ['Math. analysis']

Steve = Reviewer('Steve', 'Rogers')
Steve.courses_attached += ['Python']
Steve.courses_attached += ['GIT']
Steve.courses_attached += ['English for pro']

Clinton = Reviewer('Clinton', 'Barton')
Clinton.courses_attached += ['Python']
Clinton.courses_attached += ['GIT']
Clinton.courses_attached += ['Math. analysis']

Wanda.rate_l(Anthony, 'Python', 10)
Wanda.rate_l(Anthony, 'GIT', 10)
Wanda.rate_l(Anthony, 'English for pro', 10)
Wanda.rate_l(Stephen, 'Python', 8)
Wanda.rate_l(Stephen, 'GIT', 7)

Scott.rate_l(Anthony, 'Python', 10)
Scott.rate_l(Anthony, 'GIT', 10)
Scott.rate_l(Stephen, 'Python', 10)
Scott.rate_l(Stephen, 'GIT', 10)
Scott.rate_l(Stephen, 'Math. analysis', 9)

Steve.rate_hw(Wanda, 'Python', 9)
Steve.rate_hw(Wanda, 'GIT', 8)
Steve.rate_hw(Wanda, 'English for pro', 10)
Steve.rate_hw(Scott, 'Python', 7)
Steve.rate_hw(Scott, 'GIT', 6)

Clinton.rate_hw(Wanda, 'Python', 9)
Clinton.rate_hw(Wanda, 'GIT', 10)
Clinton.rate_hw(Scott, 'Python', 8)
Clinton.rate_hw(Scott, 'GIT', 9)
Clinton.rate_hw(Scott, 'Math. analysis', 5)

print(Wanda < Scott)
print(Stephen < Anthony)

print(Wanda, "\n")
print(Scott, "\n")
print(Anthony, "\n")
print(Stephen, "\n")

def all_students_avarage_grade():
    avar_student_grade = {}
    for student in Student.students_list:
        for c, gr in student.grades.items():
            for g in gr:
                avar_student_grade.setdefault(c, []).append(g)
    for c, gr in avar_student_grade.items():
        grade_sum = 0
        grade_l = len(gr)
        for g in gr:
            grade_sum += g
        avar_gr = grade_sum / grade_l
        avar_student_grade[c] = avar_gr
    res = ', '.join([f'{key.capitalize()} : {value}' for key, value in avar_student_grade.items()])
    return f'Средняя оценка студентов за домашние задания в рамках изучаемых курсов: \n{res}'

def all_lecturer_avarage_grade():
    avar_lecturer_grade = {}
    for lecturer in Lecturer.lecturer_list:
        for c, gr in lecturer.grades.items():
            for g in gr:
                avar_lecturer_grade.setdefault(c, []).append(g)
    for c, gr in avar_lecturer_grade.items():
        grade_sum = 0
        grade_l = len(gr)
        for g in gr:
            grade_sum += g
        avar_gr = grade_sum / grade_l
        avar_lecturer_grade[c] = avar_gr
    res = ', '.join([f'{key.capitalize()} : {value}' for key, value in avar_lecturer_grade.items()])
    return f'Средняя оценка лекторов за лекции в рамках читаемых курсов: \n{res}'

all_students_avarage_grade()
all_lecturer_avarage_grade()