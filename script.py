from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
stacks.append(left_stack)
middle_stack = Stack("Middle")
stacks.append(middle_stack)
right_stack = Stack("Right")
stacks.append(right_stack)
#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
for i in range(num_disks, 0, -1):
  left_stack.push(i)
num_optimal_moves = 2**(num_disks)-1
print("\nThe fastest you can solve this game is in {opt} moves".format(opt=num_optimal_moves))

  

#Get User Input
def get_input():
  choices = [(i.get_name())[0] for i in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {let} for {name}".format(let=letter, name=name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
        
        
      
      
        
#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for i in stacks:
    i.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
print("\n\nYou completed the game in {o} moves, and the optimal number of moves is {i}".format(o=num_user_moves, i=num_optimal_moves))

      
      
      
    
    