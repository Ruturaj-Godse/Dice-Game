def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    # write your code here
    for num1 in dice1:
        for num2 in dice2:
            if num1 > num2:
                dice1_wins+=1
            elif num2 > num1:
                dice2_wins+=1

    return (dice1_wins, dice2_wins)

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    # write your code here
    # use your implementation of count_wins method if necessary
    for dice1_ind in range(len(dices)):
        wins = 0
        dice1 = dices[dice1_ind]
        for dice2_ind in range(len(dices)):
            dice2 = dices[dice2_ind]
            if dice1_ind==dice2_ind:
                continue
            w1, w2 = count_wins(dice1, dice2)
            if w1>w2:
                wins+=1
        if wins==len(dices)-1:
            return dice1_ind

    return -1

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    best_dice = find_the_best_dice(dices)
    if best_dice!=-1:
        strategy["first_dice"] = best_dice
        return strategy

    strategy["choose_first"] = False
    for i in range(len(dices)):
        strategy[i] = i

    for i in range(len(dices)):
        for j in range(len(dices)):
            if i==j:
                continue
            w1, w2 = count_wins(dices[i], dices[j])
            if w2>w1:
                w1, w3 = count_wins(dices[i], dices[strategy[i]])
                if w2>w3:
                    strategy[i] = j
    # write your code here

    return strategy


n = int(input())
dices = []
for i in range(n):
    dice = list(map(int, input().split()))
    dices.append(dice)

print(compute_strategy(dices))
