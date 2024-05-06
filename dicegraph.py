import matplotlib.pyplot as plt

def roll_dice(num_dice):
    outcomes = [0] * (6*num_dice + 1)
    for i in range(1, 7):
        outcomes[i] = 1 / 6**num_dice
    for die in range(2, num_dice + 1):
        new_outcomes = [0] * (6*num_dice + 1)
        for i in range(1, len(outcomes)):
            for j in range(1, 7):
                if i + j < len(new_outcomes):
                    new_outcomes[i + j] += outcomes[i] / 6
        outcomes = new_outcomes
    return outcomes

def plot_dice_probabilities(num_dice):
    outcomes = roll_dice(num_dice)
    plt.bar(range(num_dice, 6*num_dice + 1), outcomes[num_dice:])
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Rolling {} Dice'.format(num_dice))
    plt.show()

plot_dice_probabilities(10)
