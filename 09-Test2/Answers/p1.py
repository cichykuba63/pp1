def f(player1,player2):
    sum_player1 = 0; sum_player2 = 0
    dic = {
        "A": 10,
        "K": 10,
        "Q": 10,
        "J": 10,
        "T": 10
    }

    for letter in player1:
        if dic.get(letter) == None:
            sum_player1 += int(letter)
        else:
            sum_player1 += dic[letter]

    for letter in player2:
        if dic.get(letter) == None:
            sum_player2 += int(letter)
        else:
            sum_player2 += dic[letter]

    if sum_player1 > sum_player2:
        return True
    else:
        return False
