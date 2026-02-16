names=[]
score=[]
while names != 'END':
      names = input('Enter your name("END" to stop input): ')
      score = input('Enter your score: ')
stn= dict(names)
stsc= dict(score)
print(f'{"Student Name"} {"Grade":>21}\n'
      f'{"-"*15}{"-"*5:>21}')
