# beat-your-neighbour
Python script to simulate this 2-player card game.

This is based on:

1. The Wikipedia article:

   Beat Your Neighbour (aka Beggar my neighbour) - https://en.wikipedia.org/wiki/Beggar-my-neighbour

2. A script I wrote (byn.py) to simulate the game.

### Simulation Results

#### 1,000 Games
![1,000 Games](byn-1000.png)

#### 10,000 Games
![10,000 Games](byn-10000.png)

#### 100,000 Games
![100,000 Games](byn-100000.png)

#### 1000,000 Games
![1,000,000 Games](byn-1000000.png)

#### The effect of changing Court Cards: JQKA vs JQK vs JQ vs J
The following table shows that with <b>less court cards</b>, the average game is longer (mean turns increases) but the flip length (mean flips) reduces.

| Court Cards | Min Turns | Max Turns  | Mean Turns | Min Flips | Max Flips | Mean Flips |
| ----------: | --------: | ---------: | ---------: | --------: | --------: | ---------: |
|        JQKA |         9 |        700 |     108.51 |         4 |        26 |      12.31 |
|        JQK  |        21 |      1,518 |     214.94 |         3 |        18 |       7.83 |
|        JQ   |        35 |      2,994 |     374.03 |         2 |         9 |       4.42 |
|        J    |        47 |      3,710 |     614.19 |         1 |         4 |       1.98 |


### Help
```
$ python byn.py -h
usage: byn.py [-h] [-n GAMES] [-d] [-l LEVEL] [-q] [-s]

This program simulates a 2-player game of Beat Thy Neighbour.

optional arguments:
  -h, --help            show this help message and exit
  -n GAMES, --games GAMES
                        no of games to play
  -d, --debug           print some debugging output
  -l LEVEL, --level LEVEL
                        print debug level
  -q, --quiet           supress gameplay
  -s, --step            step through each turn
$
```

### Sample run
```
$ python byn.py
Beat Your Neighbour, 2-Player Card Game Simulation
Court cards: JQKA

Game: 1
Initial Hand1(26)
10♣  5♥  10♦  K♣  3♣  K♠  4♥  5♣  7♣  J♣  7♦  2♦  8♥
Q♣  9♦  6♦  3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦

Initial Hand2(26)
4♦  8♣  4♣  7♠  8♦  K♦  9♠  6♠  3♦  5♦  2♥  J♠  A♠
4♠  5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 1 Player 1 plays: 10♣
Pile(1)
10♣

Hand1(25)
5♥  10♦  K♣  3♣  K♠  4♥  5♣  7♣  J♣  7♦  2♦  8♥  Q♣
9♦  6♦  3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦

Hand2(26)
4♦  8♣  4♣  7♠  8♦  K♦  9♠  6♠  3♦  5♦  2♥  J♠  A♠
4♠  5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 2 Player 2 plays: 4♦
Pile(2)
10♣  4♦

Hand1(25)
5♥  10♦  K♣  3♣  K♠  4♥  5♣  7♣  J♣  7♦  2♦  8♥  Q♣
9♦  6♦  3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦

Hand2(25)
8♣  4♣  7♠  8♦  K♦  9♠  6♠  3♦  5♦  2♥  J♠  A♠  4♠
5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 3 Player 1 plays: 5♥
Pile(3)
10♣  4♦  5♥

Hand1(24)
10♦  K♣  3♣  K♠  4♥  5♣  7♣  J♣  7♦  2♦  8♥  Q♣  9♦
6♦  3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦

Hand2(25)
8♣  4♣  7♠  8♦  K♦  9♠  6♠  3♦  5♦  2♥  J♠  A♠  4♠
5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 4 Player 2 plays: 8♣
Pile(4)
10♣  4♦  5♥  8♣

Hand1(24)
10♦  K♣  3♣  K♠  4♥  5♣  7♣  J♣  7♦  2♦  8♥  Q♣  9♦
6♦  3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦

Hand2(24)
4♣  7♠  8♦  K♦  9♠  6♠  3♦  5♦  2♥  J♠  A♠  4♠  5♠
10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 5 Player 1 plays: 10♦
Pile(5)
10♣  4♦  5♥  8♣  10♦

Hand1(23)
K♣  3♣  K♠  4♥  5♣  7♣  J♣  7♦  2♦  8♥  Q♣  9♦  6♦
3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦

Hand2(24)
4♣  7♠  8♦  K♦  9♠  6♠  3♦  5♦  2♥  J♠  A♠  4♠  5♠
10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 6 Player 2 plays: 4♣
Pile(6)
10♣  4♦  5♥  8♣  10♦  4♣

Hand1(23)
K♣  3♣  K♠  4♥  5♣  7♣  J♣  7♦  2♦  8♥  Q♣  9♦  6♦
3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦

Hand2(23)
7♠  8♦  K♦  9♠  6♠  3♦  5♦  2♥  J♠  A♠  4♠  5♠  10♠
2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 7 Player 1 plays: K♣
Cost is 3, Player 2 paying 7♠
Cost is 3, Player 2 paying 8♦
Cost is 3, Player 2 paying K♦
Cost is 3, Player 1 paying 3♣
Cost is 3, Player 1 paying K♠
Cost is 3, Player 2 paying 9♠
Cost is 3, Player 2 paying 6♠
Cost is 3, Player 2 paying 3♦
Turn winner is player 1
Hand1(35)
4♥  5♣  7♣  J♣  7♦  2♦  8♥  Q♣  9♦  6♦  3♥  10♥  8♠
Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣
K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦

Hand2(17)
5♦  2♥  J♠  A♠  4♠  5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥
7♥  A♥  6♣  J♥

Turn: 8 Player 1 plays: 4♥
Pile(1)
4♥

Hand1(34)
5♣  7♣  J♣  7♦  2♦  8♥  Q♣  9♦  6♦  3♥  10♥  8♠  Q♠
J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣  K♣
7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦

Hand2(17)
5♦  2♥  J♠  A♠  4♠  5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥
7♥  A♥  6♣  J♥

Turn: 9 Player 2 plays: 5♦
Pile(2)
4♥  5♦

Hand1(34)
5♣  7♣  J♣  7♦  2♦  8♥  Q♣  9♦  6♦  3♥  10♥  8♠  Q♠
J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣  K♣
7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦

Hand2(16)
2♥  J♠  A♠  4♠  5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥
A♥  6♣  J♥

Turn: 10 Player 1 plays: 5♣
Pile(3)
4♥  5♦  5♣

Hand1(33)
7♣  J♣  7♦  2♦  8♥  Q♣  9♦  6♦  3♥  10♥  8♠  Q♠  J♦
A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣  K♣  7♠
8♦  K♦  3♣  K♠  9♠  6♠  3♦

Hand2(16)
2♥  J♠  A♠  4♠  5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥
A♥  6♣  J♥

Turn: 11 Player 2 plays: 2♥
Pile(4)
4♥  5♦  5♣  2♥

Hand1(33)
7♣  J♣  7♦  2♦  8♥  Q♣  9♦  6♦  3♥  10♥  8♠  Q♠  J♦
A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣  K♣  7♠
8♦  K♦  3♣  K♠  9♠  6♠  3♦

Hand2(15)
J♠  A♠  4♠  5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥
6♣  J♥

Turn: 12 Player 1 plays: 7♣
Pile(5)
4♥  5♦  5♣  2♥  7♣

Hand1(32)
J♣  7♦  2♦  8♥  Q♣  9♦  6♦  3♥  10♥  8♠  Q♠  J♦  A♦
6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣  K♣  7♠  8♦
K♦  3♣  K♠  9♠  6♠  3♦

Hand2(15)
J♠  A♠  4♠  5♠  10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥
6♣  J♥

Turn: 13 Player 2 plays: J♠
Cost is 1, Player 1 paying J♣
Cost is 1, Player 2 paying A♠
Cost is 4, Player 1 paying 7♦
Cost is 4, Player 1 paying 2♦
Cost is 4, Player 1 paying 8♥
Cost is 4, Player 1 paying Q♣
Cost is 2, Player 2 paying 4♠
Cost is 2, Player 2 paying 5♠
Turn winner is player 1
Hand1(41)
9♦  6♦  3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣
4♦  5♥  8♣  10♦  4♣  K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠
3♦  4♥  5♦  5♣  2♥  7♣  J♠  J♣  A♠  7♦  2♦  8♥  Q♣
4♠  5♠

Hand2(11)
10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 14 Player 1 plays: 9♦
Pile(1)
9♦

Hand1(40)
6♦  3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦
5♥  8♣  10♦  4♣  K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦
4♥  5♦  5♣  2♥  7♣  J♠  J♣  A♠  7♦  2♦  8♥  Q♣  4♠
5♠

Hand2(11)
10♠  2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 15 Player 2 plays: 10♠
Pile(2)
9♦  10♠

Hand1(40)
6♦  3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦
5♥  8♣  10♦  4♣  K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦
4♥  5♦  5♣  2♥  7♣  J♠  J♣  A♠  7♦  2♦  8♥  Q♣  4♠
5♠

Hand2(10)
2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 16 Player 1 plays: 6♦
Pile(3)
9♦  10♠  6♦

Hand1(39)
3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥
8♣  10♦  4♣  K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦  4♥
5♦  5♣  2♥  7♣  J♠  J♣  A♠  7♦  2♦  8♥  Q♣  4♠  5♠

Hand2(10)
2♣  2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 17 Player 2 plays: 2♣
Pile(4)
9♦  10♠  6♦  2♣

Hand1(39)
3♥  10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥
8♣  10♦  4♣  K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦  4♥
5♦  5♣  2♥  7♣  J♠  J♣  A♠  7♦  2♦  8♥  Q♣  4♠  5♠

Hand2(9)
2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 18 Player 1 plays: 3♥
Pile(5)
9♦  10♠  6♦  2♣  3♥

Hand1(38)
10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣
10♦  4♣  K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦  4♥  5♦
5♣  2♥  7♣  J♠  J♣  A♠  7♦  2♦  8♥  Q♣  4♠  5♠

Hand2(9)
2♠  K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 19 Player 2 plays: 2♠
Pile(6)
9♦  10♠  6♦  2♣  3♥  2♠

Hand1(38)
10♥  8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣
10♦  4♣  K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦  4♥  5♦
5♣  2♥  7♣  J♠  J♣  A♠  7♦  2♦  8♥  Q♣  4♠  5♠

Hand2(8)
K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 20 Player 1 plays: 10♥
Pile(7)
9♦  10♠  6♦  2♣  3♥  2♠  10♥

Hand1(37)
8♠  Q♠  J♦  A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣  10♦
4♣  K♣  7♠  8♦  K♦  3♣  K♠  9♠  6♠  3♦  4♥  5♦  5♣
2♥  7♣  J♠  J♣  A♠  7♦  2♦  8♥  Q♣  4♠  5♠

Hand2(8)
K♥  Q♥  9♣  9♥  7♥  A♥  6♣  J♥

Turn: 21 Player 2 plays: K♥
Cost is 3, Player 1 paying 8♠
Cost is 3, Player 1 paying Q♠
Cost is 2, Player 2 paying Q♥
Cost is 2, Player 1 paying J♦
Cost is 1, Player 2 paying 9♣
Turn winner is player 1
Hand1(47)
A♦  6♥  A♣  3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣  K♣  7♠
8♦  K♦  3♣  K♠  9♠  6♠  3♦  4♥  5♦  5♣  2♥  7♣  J♠
J♣  A♠  7♦  2♦  8♥  Q♣  4♠  5♠  9♦  10♠  6♦  2♣  3♥
2♠  10♥  K♥  8♠  Q♠  Q♥  J♦  9♣

Hand2(5)
9♥  7♥  A♥  6♣  J♥

Turn: 22 Player 1 plays: A♦
Cost is 4, Player 2 paying 9♥
Cost is 4, Player 2 paying 7♥
Cost is 4, Player 2 paying A♥
Cost is 4, Player 1 paying 6♥
Cost is 4, Player 1 paying A♣
Cost is 4, Player 2 paying 6♣
Cost is 4, Player 2 paying J♥
Hand1(44)
3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣  K♣  7♠  8♦  K♦  3♣
K♠  9♠  6♠  3♦  4♥  5♦  5♣  2♥  7♣  J♠  J♣  A♠  7♦
2♦  8♥  Q♣  4♠  5♠  9♦  10♠  6♦  2♣  3♥  2♠  10♥  K♥
8♠  Q♠  Q♥  J♦  9♣

Hand2(0)


Game over! Winner is player 2
Final Pile(8)
A♦  9♥  7♥  A♥  6♥  A♣  6♣  J♥

Final Hand1(44)
3♠  Q♦  10♣  4♦  5♥  8♣  10♦  4♣  K♣  7♠  8♦  K♦  3♣
K♠  9♠  6♠  3♦  4♥  5♦  5♣  2♥  7♣  J♠  J♣  A♠  7♦
2♦  8♥  Q♣  4♠  5♠  9♦  10♠  6♦  2♣  3♥  2♠  10♥  K♥
8♠  Q♠  Q♥  J♦  9♣

Final Hand2(0)


23 turns, longest penalty run 9
$
```
