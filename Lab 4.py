names = []
score = []
studentgrades = {}
while names != 'END':
      names = input('Enter your name("END" to stop input): ')
      score = input('Enter your score: ')
      for names, score in studentgrades:
            studentgrades.update({names: score})
print(f'Class average score is {sum(studentgrades.values)/len(studentgrades.values):.f}\n'
      f'Highest score is {max(studentgrades.values()):.f} achieved by {studentgrades.key()}\n'
      f'{"Student Name"} {"Grade":>21}\n'
      f'{"-"*15}{"-"*5:>21}\n'
      f'{names[0]}{score[0]:>21}\n'
      f'{names[1]}{score[1]:>21}\n'
      f'{names[2]}{score[2]:>21}\n'
      f'{names[3]}{score[3]:>21}\n')
