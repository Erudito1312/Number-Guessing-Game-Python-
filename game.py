import random
import os

def gamelog():
  ans = input()
  while not ans.isdigit():
    print('It has to be a number!')
    ans = input()
  ans = int(ans)
  return ans

def playgame():
  n = 0
  x = random.randint(1, 100)
  print(f'Current record: {best} tries')
  print('Guess a number from 1 to 100')
  guess = gamelog()

  while guess != x:
    if guess > x:
      print('Lower')
      n += 1
      guess = gamelog()
    else:
      print('Higher')
      guess = gamelog()
      n += 1
  print('Correct!')
  return n + 1

def replay():
    print('Wanna go again? Type Y if yes, or N if no')
    answer = input().lower()
    while answer not in ('y', 'n'):
      print('What? I said Y or N!')
      answer = input().lower()
    return answer

#code

score_path = 'Score.txt'

if os.path.isfile(score_path):
  with open(score_path, "r") as score:
    content = score.read()
    if content.isdigit():
      best = int(content)
    else:
      best = 100
else:
  with open(score_path, "w") as score:
    best = 100
    score.write(str(best))

while True:
  tries = playgame()

  if tries < best:
    best = tries
    with open(score_path, "w") as score:
      score.write(str(best))

  print(f'It took you {tries} tries!')
  print(f'Personal best is {best}')

  if replay() == 'n':
    print('Have a good day!')

    break

