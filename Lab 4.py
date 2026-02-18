students = {}
name = []
score = []
while True:
      name = input('Enter your name("END" to stop input): ')
      if name == 'END':
            break
      score = float(input('Enter your score: '))
      students[name]=score
highest_name = max(students, key=students.get)
highest_score = students[highest_name]
class_average = sum(students.values())/len(students)
print(f'Class average score is {class_average:.1f}\n'
      f'Highest score is {highest_score:.1f} achieved by {highest_name}\n'
      f'{"Student Name"} {"Grade":>8}\n'
      f'{"-"*15}{"-"*5:>6}')
for name, score in students.items():
      print(f'{name:17}{score:.1f}')
