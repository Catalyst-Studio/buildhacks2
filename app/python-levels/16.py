Player1Hand = ['Seven', 'Nine']
Player1Score = 0
Player2Hand = ('Three', 'King')
Player2Score == 0
CardWeight = ['Ace', 'Two', 'Three' 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack','Queen', 'King']
for card in range(0, 2):
    for count in range(0, 13):
        if Player1Hand[card] == CardWeight[count]:
            Player1Score += count + 1
        if Player2Hand[card] == CardWeight[count]:
            Player2Score += count + 1

    if Player1Hand[card] == 'King':
        if Player2Hand[card] == 'Ace':
            Player2Score += 13
    if Player2Hand[cards] == 'King':
        if Player1Hand[card] = 'Ace':
            Player1Score =+ 13
print("Player 1 Score: " Player1Score " vs " "Player 2 Score: ", Player2Score)