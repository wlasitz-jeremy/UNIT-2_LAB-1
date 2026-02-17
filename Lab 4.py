names = []
score = []
studentgrades = {}
while names != 'END':
      names = input('Enter your name("END" to stop input): ')
      score = input('Enter your score: ')
      studentgrades.update({names:score})
print(f'Class average score is {sum(score)/len(score):.f}\n'
      f'Highest score is {max(score):.f} achieved by {names}\n'
      f'{"Student Name"} {"Grade":>21}\n'
      f'{"-"*15}{"-"*5:>21}\n'
      f'{names[0]}{score[0]:>21}\n'
      f'{names[1]}{score[1]:>21}\n'
      f'{names[2]}{score[2]:>21}\n'
      f'{names[3]}{score[3]:>21}\n')










