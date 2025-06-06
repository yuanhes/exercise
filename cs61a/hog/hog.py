"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.

    >>> test_dice = make_test_dice(1, 2, 3)
    >>> roll_dice(3, test_dice)
    1
    >>> test_dice()
    1
    >>> roll_dice(2, test_dice)
    5
    >>> test_dice = make_test_dice(3, 3, 3, 3)
    >>> roll_dice(4, test_dice)
    12
    >>> a = roll_dice(10, make_test_dice(5))
    >>> a
    50
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls > 0, "Must roll at least once."
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    i , score, sow_sad = 0, 0, False
    while i < num_rolls:
        points = dice()
        if not sow_sad:
            if points == 1:
                sow_sad = True
            score += points
        i += 1

    if sow_sad:
        return 1
    else:
        return score
    # END PROBLEM 1

def boar_brawl(player_score, opponent_score):
    """Return the points scored when the current player rolls 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    >>> boar_brawl(21, 46)
    9
    >>> boar_brawl(45, 52)
    1
    >>> boar_brawl(2, 5)
    6
    >>> a = boar_brawl(129, 116)
    >>> a
    24
    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    a = player_score % 10
    b = opponent_score // 10 % 10
    return max(3 * abs(a - b), 1)
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    current player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.

    >>> take_turn(0, 21, 46)
    9
    >>> take_turn(3, 21, 46, make_test_dice(3, 2, 1))
    1
    >>> a = take_turn(2, 21, 46, make_test_dice(3, 2, 1))
    >>> a
    5
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls >= 0, "Cannot roll a negative number of dice in take_turn."
    assert num_rolls <= 10, "Cannot roll more than 10 dice."
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        return boar_brawl(player_score, opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score


def is_prime(n):
    """Return whether N is prime."""
    assert type(n) == int and n > 0 , "n must be a positive integer."

    if n == 1:
        return False
    k = 2
    threshold = int(n ** 0.5)
    while k <= threshold:
        if n % k == 0:
            return False
        k += 1
    return True


def num_factors(n):
    """Return the number of factors of N, including 1 and N itself.
    
    >>> num_factors(1)
    1
    >>> num_factors(2)
    2
    >>> num_factors(9)
    3
    >>> num_factors(12)
    6
    """
    assert type(n) == int and n > 0 , "n must be a positive integer."
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    k, count = 2, 2
    threshold = n // 2
    while k <= threshold:
        if n % k == 0:
            count += 1
        k += 1
    return count
    # END PROBLEM 4


def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule.
    
    >>> sus_points(5)
    5
    >>> sus_points(21)
    23
    >>> sus_points(12)
    12
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if num_factors(score) in [3, 4]:
        while not is_prime(score):
            score += 1
    return score
    # END PROBLEM 4


def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.

    >>> sus_update(0, 21, 46, make_test_dice(3, 2, 1))
    30
    >>> sus_update(3, 21, 46, make_test_dice(3, 2, 1))
    23
    >>> sus_update(2, 21, 46, make_test_dice(3, 2, 1))
    29
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    score = sus_points(score)
    return score
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update, score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while (score0 < goal) and (score1 < goal):
        if who == 0:
            score0 = update(strategy0(score0, score1), score0, score1, dice)
        else:
            score1 = update(strategy1(score1, score0), score1, score0, dice)
        who = 1 - who
        #print("DEBUG:", score0, score1)
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10

    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    def strategy(a, b):
        return n
    return strategy
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> catch_up(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    for every possible combination of score and opponent_score
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    num_init = strategy(0, 0)
    i = 0
    while i < goal:
        j = 0
        while j < goal:
            if strategy(i, j) != num_init:
                return False
            j += 1
        i += 1
    return True
    # END PROBLEM 7


def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """

    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def averaged_function(*args):
        i, total = 0, 0
        while i < times_called:
            total += original_function(*args)
            i += 1
        return total / times_called
    return averaged_function
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, times_called=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    averaged_roll_dice = make_averaged(roll_dice, times_called)
    i, max_score = 1, -1
    while i <= 10:
        score = averaged_roll_dice(i, dice)
        if score > max_score:
            num_rolls = i
            max_score = score
        i += 1
    return num_rolls
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print("Max scoring num rolls for six-sided dice:", six_sided_max)

    print("always_roll(6) win rate:", average_win_rate(always_roll(6)))  # near 0.5
    print("catch_up win rate:", average_win_rate(catch_up))
    print("always_roll(3) win rate:", average_win_rate(always_roll(3)))
    print("always_roll(5) win rate:", average_win_rate(always_roll(5)))
    print("always_roll(8) win rate:", average_win_rate(always_roll(8)))
    print("always_roll(10) win rate:", average_win_rate(always_roll(10)))

    print("boar_strategy win rate:", average_win_rate(boar_strategy))
    print("sus_strategy win rate:", average_win_rate(sus_strategy))
    print("final_strategy win rate:", average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"




def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore the Sus Fuss rule.
    """
    # BEGIN PROBLEM 10
    if boar_brawl(score, opponent_score) >= threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when rolling 0 increases the score by at least
    THRESHOLD points, and returns NUM_ROLLS otherwise. Consider both the Boar Brawl and
    Suss Fuss rules."""
    # BEGIN PROBLEM 11
    if sus_points(score + boar_brawl(score, opponent_score)) - score >= threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 11

def calc_roll_expectations(max_num_rolls=10, dice=six_sided):
    """Calculate the expectation of rolls with num_rolls from 1 to max_num_rolls
    """
    expectations = []
    averaged_roll_dice = make_averaged(roll_dice)
    i = 1
    while i < max_num_rolls:
        expectations += [averaged_roll_dice(i, dice)]
        i += 1
    return expectations

ROLL_EXPECTATIONS = calc_roll_expectations()

def roll_expectation(num_rolls):
    assert type(num_rolls) == int and num_rolls > 0 and num_rolls <= 10, "num_rolls must be positive integer less than 10. "
    return ROLL_EXPECTATIONS[num_rolls - 1]

def final_strategy(score, opponent_score, goal=GOAL, num_rolls=6):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    if sus_points(score + boar_brawl(score, opponent_score)) >= goal:
        return 0 
    i = 1
    while i < num_rolls:
        if score + roll_expectation(i) >= goal:
            return i
        i += 1
    if sus_points(score + boar_brawl(score, opponent_score)) - score >= roll_expectation(num_rolls):
        return 0
    else:
        return num_rolls
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument(
        "--run_experiments", "-r", action="store_true", help="Runs strategy experiments"
    )

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
