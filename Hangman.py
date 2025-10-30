import random

word_list = ["aardvark", "baboon", "camel"]
chose_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chose_word}.')

display = []

for i in range(len(chose_word)):
    display += "_"
  
print(display)
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
  guess = input("Please choose a letter ").lower()
  for position in range(len(chose_word)):
    letter = chose_word[position]
  if letter == guess:
    display[position] = letter

print(display)