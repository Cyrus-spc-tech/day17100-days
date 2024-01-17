from getpass import getpass as input


print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

player1_score = 0
player2_score = 0

while True: 
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()

  if(player1Move=="R"):
    if(player2Move=="R"):
      print("draw!")
    elif(player2Move=="S"):
      print("Player1 Win")
      player1_score += 1
    elif(player2Move=="P"):
      print(" Player2 win")
      player2_score += 1
  elif(player1Move=="P"):
    if(player2Move=="R"):
      print("Player1 Win")
      player1_score += 1
    elif(player2Move=="S"):
      print("Player2 Win")
      player2_score += 1
    elif(player2Move=="P"):
      print(" Draw.")
  elif(player1Move=="S"):
    if(player2Move=="R"):
      print("Player 2 Win ")
      player2_score += 1
    elif(player2Move=="S"):
      print("Draw.")
    elif(player2Move=="P"):
      print("Player1 Win")
      player1_score += 1

  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:
    continue