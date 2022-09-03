Player1Hand = ['Ace', 'King']
Player1Score = 0
Player2Hand = ['Two', 'Two']
Player2Score = 0
Dealer = ['Queen', 'Jack', 'Ten']
CardWeight = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']
for card in range(0, len(Player1Hand)):
    for count in range(0, 13):
        if Player1Hand[card] == CardWeight[count]:
            Player1Score += count