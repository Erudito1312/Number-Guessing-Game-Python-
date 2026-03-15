import random

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
  print(f'It took you {n + 1} tries!')

def replay():
    print('Wanna go again? Type Y if yes, or N if no')
    answer = input().lower()
    while answer not in ('y', 'n'):
      print('What? I said Y or N!')
      answer = input().lower()
    return answer

#code

while True:
  playgame()
  if replay() == 'n':
    print('Have a good day!')
    break

