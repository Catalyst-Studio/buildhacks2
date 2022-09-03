Player1Hand = ['Ace', 'King']
Player1Score = 0
Player2Hand = ['Two', 'Two']
Player2Score = 0
CardWeight = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack','Queen', 'King', 'Ace']
for card in range(0, 2):
    for count in range(0, 13):
        if Player1Hand[card] == CardWeight[count]:
            Player1Score += count
            print(Player1Score)
        if Player2Hand[card] == CardWeight[count]:
            Player2Score += count
            print(Player2Score)