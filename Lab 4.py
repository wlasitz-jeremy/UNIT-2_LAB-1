names=[]
score=[]
while names != 'END':
      names = input('Enter your name("END" to stop input): ')
      score = input('Enter your score: ')
print(f'Class average score is {sum(score)/len(score):.f}\n'
      f'Highest score is {max(score):.f}\n'
      f'{"Student Name"} {"Grade":>21}\n'
      f'{"-"*15}{"-"*5:>21}\n')
