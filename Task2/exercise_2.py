# You have first 5 best tennis players according APT rankings
# Set the first-place player to last place and vice versa

players = ['Ashleigh Barty', 'Simona Halep', 'Naomi Osaka',
           'Karolina Pliskova', 'Elina Svitolina']


def change_postitions(players: list):
    players[0], players[-1] = players[-1], players[0]
    print(players)


if __name__ == '__main__':
    change_postitions(players)
