class Student:

     def __init__(self, name, age, grade, scores):
         self.name = name
         self.age = age
         self.grade = grade
         self.scores = scores

     def info(self):
         print('Имя', self.name)
         print('Возраст', self.age)
         print('Класс', self.grade)
         print('Оценки', self.scores)

     def average_score(self):
        return sum(self.scores) / len(self.scores)


student2 = Student("Алексей", 13, "6", [5, 4, 4, 5])
student2.info()
print(student2.average_score())
