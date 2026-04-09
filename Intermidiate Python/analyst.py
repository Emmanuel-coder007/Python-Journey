# Write code below 💖
player1 = {'name':'Kyle', 'position':'center back', 'jersey number': 0, 'yards_gained': 150, 'touchdowns': 2}
player2 = {'name':'Dave', 'position':'right back', 'jersey number': 12, 'yards_gained': 250, 'touchdowns': 3}
player3 = {'name':'Niel', 'position':'center forward', 'jersey number': 79, 'yards_gained': 50, 'touchdowns': 6}
player4 = {'name':'Omar', 'position':'center', 'jersey number': 2, 'yards_gained': 100, 'touchdowns': 1}
player5 = {'name':'Teo', 'position':'center', 'jersey number': 7, 'yards_gained': 700, 'touchdowns': 7}

print(player1['position'])
print(player2['position'])
print(player3['position'])
print(player4['position'])
print(player5['position'])

player2['position'] = 'right forward'
print(player2['position'])


average_yard = (player1['yards_gained'] + player2['yards_gained'] + player3['yards_gained'] +player4['yards_gained'] + player5['yards_gained'])/5

average_touchdown = (player1['touchdowns'] + player2['touchdowns'] + player3['touchdowns'] + player4['touchdowns'] + player5['touchdowns'])/5

print(f'Average Yard: {average_yard} while Aeverage Touchdown: {average_touchdown}')