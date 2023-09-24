import random
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
import time

"""
  byn.py

  Description:
    This script simulates the 2-player card game, Beat Your Neighbour.

  Author: Mike Smith

  Modification History:
  17-Sep-2023 - Initial Version.
  18-Sep-2023 - Added functions to help break it down.
  23-Sep-2023 - Add -n for number of games.
                Add -q to just show charts of multiple runs with min/max and mean stats of turns and flips.
                A turn is the complete turn of a single player who either starts the game or wins the previous trick.
                A flip is when a payout flips from one player back to the other, which can happen multiple times randomly.
                Add -c to define the court-cards to use, "JQKA" (default), "JQK", "JQ" or "J".
                Using just the Jack ("J") seems to sometimes loop, if cycles develop.
                Add -p <secs> and -t <secs> pause delay between each game/turn.
"""
cost_dict = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}

#
# Functions.
#
def check_cards(msg, deck):
    count = 1
    print(msg + '({})'.format(len(deck)))
    wrapped = False
    for card in deck:
        print(card, ' ', end='')
        if count % 13 == 0:
            print()
            wrapped = True
        else:
            wrapped = False
        count += 1
    if not wrapped:
        print()
    print()

def is_court_card(card):
    """
    This just checks if the given card is a court card by looking at the first character.
    """
    if card[0:1] in court_cards:
        return True
    else:
        return False

def pay_penalty(hand, card, pile):
    """
    This is passed a court card played by the first player and the hand of the
    second player. It counts out the penalty cards from the hand, but stops if
    a count card turns up.

    It returns the last card turned up, which is either:
    1. the last non-court cart.
    2. another court card wherever it occurs.
    """
    cost = cost_dict[card[0:1]]
    payment = 0
    pay_card = None
    while payment < cost and len(hand) > 0:
      pay_card = hand.pop(0)
      pile.append(pay_card)
      payment += 1
      if not quiet:
          if (hand == hand1):
              print('Cost is {}, Player 1 paying {}'.format(str(cost), pay_card))
          if (hand == hand2):
              print('Cost is {}, Player 2 paying {}'.format(str(cost), pay_card))
      if (pay_pause > 0):
          time.sleep(pay_pause)
      if is_court_card(pay_card):
          break

    if len(hand) == 0:
        pay_card = None

    return payment, pay_card

def switch_hands(hand, hand1, hand2):
    """
    This just switches the players hands.
    """
    if hand == hand1:
        hand = hand2
    else:
        hand = hand1
    return hand


def take_pile(hand, hand1, hand2, pile):
    """
    This added the pile to the current hand and clears the pile.
    """
    for c in pile:
        hand.append(c)
    pile = []

    winner = None
    if hand == hand1:
        winner = '1'
    if hand == hand2:
        winner = '2'

    return (winner, hand, pile)


#
# Main Program.
#

# Check for any command line args.
parser = argparse.ArgumentParser(description='This program simulates a 2-player game of Beat Thy Neighbour.')
parser.add_argument('-n', '--games', help='no of games to play', type=int, default=1)
parser.add_argument('-c', '--cards', help='definition of the court-cards', type=str, default='JQKA')
parser.add_argument('-d', '--debug', help='print some debugging output', action='store_true')
parser.add_argument('-l', '--level', help='print debug level', type=int, default=1)
parser.add_argument('-q', '--quiet', help='supress gameplay', action='store_true')
parser.add_argument('-s', '--step', help='step through each turn', action='store_true')
parser.add_argument('-g', '--game_pause', help='pause between each game', type=int, default=4)
parser.add_argument('-t', '--turn_pause', help='pause between each turn', type=int, default=2)
args = parser.parse_args()

n = args.games
court_cards = args.cards
debug = args.debug
debug_level = args.level
quiet = args.quiet
step = args.step
game_pause = args.game_pause
turn_pause = args.turn_pause
pay_pause = turn_pause / 2
if quiet:
    game_pause = 0
    turn_pause = 0
    pay_pause = 0

if debug:
    print('Games:', n)
    print('Court cards:', court_cards)
    print('Quiet mode:', quiet)
    print('Step through each turn:', step)
    print('Pause delay between each game:', game_pause)
    print('Pause delay between each turn:', turn_pause)

# Create a deck of cards.
#suits = '-spades -diamonds -clubs -hearts'.split()
#suits = '-S -D -C -H'.split()
suits = ['♠', '♦', '♥', '♣']
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
deck = [str(rank)+ suit for suit in suits
                        for rank in ranks]

# Check it looks ok.
if debug:
    check_cards('Init', deck)

print('Beat Your Neighbour, 2-Player Card Game Simulation')
if n > 1:
    print('Games:', n)
print('Court cards:', court_cards)
print()

# Set up arrays to count various things.
turns_per_game = []
flips_per_game = []
wins_p1 = 0
wins_p2 = 0

games = 0
while games < n:
    games += 1
    if not quiet:
        print('Game:', games)

    # Shuffle the cards.
    random.shuffle(deck)

    # Check it looks shuffled.
    if debug:
        check_cards('Shuffled', deck)

    # Now deal, by splitting the deck into 2 halves.
    hand1 = deck[:26]
    hand2 = deck[26:]

    # Check the split looks ok.
    if not quiet:
        check_cards('Initial Hand1', hand1)
        check_cards('Initial Hand2', hand2)

    # Now start the game.
    turn = 'player1'
    hand = hand1
    winner = None
    cost = 0
    pile = []
    turn_count = 1
    max_penalty_count = 0
    while len(hand1) and len(hand2) > 0:

        # Draw the top card from the player who has the turn, set by the variable hand that switches from hand1 to hand2.
        top_card = hand.pop(0)

        # Add the card to the pile.
        pile.append(top_card)

        if not quiet:
            if hand == hand1:
                print('Turn: {} Player 1 plays: {}'.format(turn_count, top_card))
            else:
                print('Turn: {} Player 2 plays: {}'.format(turn_count, top_card))

        if debug:
            print('Pile:', pile)
            check_cards('Hand', hand)
            check_cards('Hand2', hand2)

        # Switch hands.
        turn_count += 1
        hand = switch_hands(hand, hand1, hand2)

        if is_court_card(top_card):
            # The "other" player has to pay the cost in cards, but if a court card turns up, then the turn switches!
            penalty_count = 0
            while True:
                penalty_paid, top_card = pay_penalty(hand, top_card, pile)
                penalty_count += penalty_paid
                if top_card == None:
                    if len(hand1) == 0:
                        winner = '1'
                    if len(hand2) == 0:
                        winner = '2'
                    break
                if is_court_card(top_card):
                    # Switch hands.
                    hand = switch_hands(hand, hand1, hand2)
                else:
                    # Cost is paid, so the winner takes the pile.
                    hand = switch_hands(hand, hand1, hand2)
                    (winner, hand, pile) = take_pile(hand, hand1, hand2, pile)
                    if not quiet:
                        print('Turn winner is player {}'.format(winner))
                    break
            if penalty_count > max_penalty_count:
                max_penalty_count = penalty_count
        else:
            if not quiet:
                check_cards('Pile', pile)

        if not quiet:
            check_cards('Hand1', hand1)
            check_cards('Hand2', hand2)
        if step:
            input("Continue...")
        if turn_pause > 0:
            time.sleep(turn_pause)

    if not quiet:
        print('Game over! Winner is player {}'.format(winner))
        check_cards('Final Pile', pile)
        check_cards('Final Hand1', hand1)
        check_cards('Final Hand2', hand2)
        print('{} turns, longest penalty run {}'.format(turn_count, max_penalty_count+1))
    else:
        print('{},{},{}'.format(turn_count, max_penalty_count, winner))
        turns_per_game.append(turn_count)
        flips_per_game.append(max_penalty_count)
        if winner == '1':
            wins_p1 += 1
        else:
            wins_p2 += 1

    if (game_pause > 0) and (n > 1):
        time.sleep(game_pause)


if n > 1 and quiet:
    # Plot a chart of the result.
    x = np.arange(1, n+1)
    max_turns = np.max(turns_per_game)
    min_turns = np.min(turns_per_game)
    mean_turns = np.mean(turns_per_game)
    max_flips = np.max(flips_per_game)
    min_flips = np.min(flips_per_game)
    mean_flips = np.mean(flips_per_game)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.subplots_adjust(hspace=0)

    fig.set_size_inches(16, 9)

    ax1.set_title('Min/Max/Mean Turns: {:,}/{:,}/{:,} and Flips: {:,}/{:,}/{:,} over {:,} Games. Wins Player 1/Player 2: {:,}/{:,}'.format(min_turns, max_turns, mean_turns, min_flips, max_flips, mean_flips, n, wins_p1, wins_p2))
    ax1.plot(x, turns_per_game, color='blue')
    ax1.set(ylabel='Turns per Game')

    ax2.plot(x, flips_per_game, color='red')
    ax2.set(xlabel='Games', ylabel='Flips per Game')

    plt.savefig('byn.png', bbox_inches='tight', pad_inches=0.25)
    plt.show()
