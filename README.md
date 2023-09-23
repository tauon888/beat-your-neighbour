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
Hand1(26)
K♣  9♥  6♥  10♣  K♥  J♣  2♥  6♠  7♦  6♣  6♦  J♦  A♠
7♥  Q♥  3♠  10♥  K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠


Hand2(26)
4♥  3♥  K♦  3♦  4♣  8♣  5♣  A♣  7♠  2♦  J♠  2♠  2♣
J♥  9♣  3♣  5♥  8♦  4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦


0 Player 1: K♣
Cost is 3, Player 2 paying 4♥
Cost is 3, Player 2 paying 3♥
Cost is 3, Player 2 paying K♦
Cost is 3, Player 1 paying 9♥
Cost is 3, Player 1 paying 6♥
Cost is 3, Player 1 paying 10♣
Turn winner is player 2
Hand1(22)
K♥  J♣  2♥  6♠  7♦  6♣  6♦  J♦  A♠  7♥  Q♥  3♠  10♥
K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠

Hand2(30)
3♦  4♣  8♣  5♣  A♣  7♠  2♦  J♠  2♠  2♣  J♥  9♣  3♣
5♥  8♦  4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥
K♦  9♥  6♥  10♣

1 Player 2: 3♦
Pile(1)
3♦

Hand1(22)
K♥  J♣  2♥  6♠  7♦  6♣  6♦  J♦  A♠  7♥  Q♥  3♠  10♥
K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠

Hand2(29)
4♣  8♣  5♣  A♣  7♠  2♦  J♠  2♠  2♣  J♥  9♣  3♣  5♥
8♦  4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦
9♥  6♥  10♣

2 Player 1: K♥
Cost is 3, Player 2 paying 4♣
Cost is 3, Player 2 paying 8♣
Cost is 3, Player 2 paying 5♣
Turn winner is player 1
Hand1(26)
J♣  2♥  6♠  7♦  6♣  6♦  J♦  A♠  7♥  Q♥  3♠  10♥  K♠
5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠  3♦  K♥  4♣  8♣  5♣


Hand2(26)
A♣  7♠  2♦  J♠  2♠  2♣  J♥  9♣  3♣  5♥  8♦  4♦  8♠
Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥  6♥  10♣


3 Player 1: J♣
Cost is 1, Player 2 paying A♣
Cost is 4, Player 1 paying 2♥
Cost is 4, Player 1 paying 6♠
Cost is 4, Player 1 paying 7♦
Cost is 4, Player 1 paying 6♣
Turn winner is player 2
Hand1(21)
6♦  J♦  A♠  7♥  Q♥  3♠  10♥  K♠  5♦  8♥  A♦  5♠  4♠
Q♦  7♣  10♠  3♦  K♥  4♣  8♣  5♣

Hand2(31)
7♠  2♦  J♠  2♠  2♣  J♥  9♣  3♣  5♥  8♦  4♦  8♠  Q♠
A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥  6♥  10♣  J♣
A♣  2♥  6♠  7♦  6♣

4 Player 2: 7♠
Pile(1)
7♠

Hand1(21)
6♦  J♦  A♠  7♥  Q♥  3♠  10♥  K♠  5♦  8♥  A♦  5♠  4♠
Q♦  7♣  10♠  3♦  K♥  4♣  8♣  5♣

Hand2(30)
2♦  J♠  2♠  2♣  J♥  9♣  3♣  5♥  8♦  4♦  8♠  Q♠  A♥
9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥  6♥  10♣  J♣  A♣
2♥  6♠  7♦  6♣

5 Player 1: 6♦
Pile(2)
7♠  6♦

Hand1(20)
J♦  A♠  7♥  Q♥  3♠  10♥  K♠  5♦  8♥  A♦  5♠  4♠  Q♦
7♣  10♠  3♦  K♥  4♣  8♣  5♣

Hand2(30)
2♦  J♠  2♠  2♣  J♥  9♣  3♣  5♥  8♦  4♦  8♠  Q♠  A♥
9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥  6♥  10♣  J♣  A♣
2♥  6♠  7♦  6♣

6 Player 2: 2♦
Pile(3)
7♠  6♦  2♦

Hand1(20)
J♦  A♠  7♥  Q♥  3♠  10♥  K♠  5♦  8♥  A♦  5♠  4♠  Q♦
7♣  10♠  3♦  K♥  4♣  8♣  5♣

Hand2(29)
J♠  2♠  2♣  J♥  9♣  3♣  5♥  8♦  4♦  8♠  Q♠  A♥  9♠
10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥  6♥  10♣  J♣  A♣  2♥
6♠  7♦  6♣

7 Player 1: J♦
Cost is 1, Player 2 paying J♠
Cost is 1, Player 1 paying A♠
Cost is 4, Player 2 paying 2♠
Cost is 4, Player 2 paying 2♣
Cost is 4, Player 2 paying J♥
Cost is 1, Player 1 paying 7♥
Turn winner is player 2
Hand1(17)
Q♥  3♠  10♥  K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠  3♦
K♥  4♣  8♣  5♣

Hand2(35)
9♣  3♣  5♥  8♦  4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣
4♥  3♥  K♦  9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠
6♦  2♦  J♦  J♠  A♠  2♠  2♣  J♥  7♥

8 Player 2: 9♣
Pile(1)
9♣

Hand1(17)
Q♥  3♠  10♥  K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠  3♦
K♥  4♣  8♣  5♣

Hand2(34)
3♣  5♥  8♦  4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥
3♥  K♦  9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦
2♦  J♦  J♠  A♠  2♠  2♣  J♥  7♥

9 Player 1: Q♥
Cost is 2, Player 2 paying 3♣
Cost is 2, Player 2 paying 5♥
Turn winner is player 1
Hand1(20)
3♠  10♥  K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠  3♦  K♥
4♣  8♣  5♣  9♣  Q♥  3♣  5♥

Hand2(32)
8♦  4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦
9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦
J♠  A♠  2♠  2♣  J♥  7♥

10 Player 1: 3♠
Pile(1)
3♠

Hand1(19)
10♥  K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠  3♦  K♥  4♣
8♣  5♣  9♣  Q♥  3♣  5♥

Hand2(32)
8♦  4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦
9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦
J♠  A♠  2♠  2♣  J♥  7♥

11 Player 2: 8♦
Pile(2)
3♠  8♦

Hand1(19)
10♥  K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠  3♦  K♥  4♣
8♣  5♣  9♣  Q♥  3♣  5♥

Hand2(31)
4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥
6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠
A♠  2♠  2♣  J♥  7♥

12 Player 1: 10♥
Pile(3)
3♠  8♦  10♥

Hand1(18)
K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠  3♦  K♥  4♣  8♣
5♣  9♣  Q♥  3♣  5♥

Hand2(31)
4♦  8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥
6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠
A♠  2♠  2♣  J♥  7♥

13 Player 2: 4♦
Pile(4)
3♠  8♦  10♥  4♦

Hand1(18)
K♠  5♦  8♥  A♦  5♠  4♠  Q♦  7♣  10♠  3♦  K♥  4♣  8♣
5♣  9♣  Q♥  3♣  5♥

Hand2(30)
8♠  Q♠  A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥  6♥
10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠  A♠
2♠  2♣  J♥  7♥

14 Player 1: K♠
Cost is 3, Player 2 paying 8♠
Cost is 3, Player 2 paying Q♠
Cost is 2, Player 1 paying 5♦
Cost is 2, Player 1 paying 8♥
Turn winner is player 2
Hand1(15)
A♦  5♠  4♠  Q♦  7♣  10♠  3♦  K♥  4♣  8♣  5♣  9♣  Q♥
3♣  5♥

Hand2(37)
A♥  9♠  10♦  Q♣  9♦  K♣  4♥  3♥  K♦  9♥  6♥  10♣  J♣
A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠  A♠  2♠  2♣
J♥  7♥  3♠  8♦  10♥  4♦  K♠  8♠  Q♠  5♦  8♥

15 Player 2: A♥
Cost is 4, Player 1 paying A♦
Cost is 4, Player 2 paying 9♠
Cost is 4, Player 2 paying 10♦
Cost is 4, Player 2 paying Q♣
Cost is 2, Player 1 paying 5♠
Cost is 2, Player 1 paying 4♠
Turn winner is player 2
Hand1(12)
Q♦  7♣  10♠  3♦  K♥  4♣  8♣  5♣  9♣  Q♥  3♣  5♥

Hand2(40)
9♦  K♣  4♥  3♥  K♦  9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦
6♣  7♠  6♦  2♦  J♦  J♠  A♠  2♠  2♣  J♥  7♥  3♠  8♦
10♥  4♦  K♠  8♠  Q♠  5♦  8♥  A♥  A♦  9♠  10♦  Q♣  5♠
4♠

16 Player 2: 9♦
Pile(1)
9♦

Hand1(12)
Q♦  7♣  10♠  3♦  K♥  4♣  8♣  5♣  9♣  Q♥  3♣  5♥

Hand2(39)
K♣  4♥  3♥  K♦  9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣
7♠  6♦  2♦  J♦  J♠  A♠  2♠  2♣  J♥  7♥  3♠  8♦  10♥
4♦  K♠  8♠  Q♠  5♦  8♥  A♥  A♦  9♠  10♦  Q♣  5♠  4♠


17 Player 1: Q♦
Cost is 2, Player 2 paying K♣
Cost is 3, Player 1 paying 7♣
Cost is 3, Player 1 paying 10♠
Cost is 3, Player 1 paying 3♦
Turn winner is player 2
Hand1(8)
K♥  4♣  8♣  5♣  9♣  Q♥  3♣  5♥

Hand2(44)
4♥  3♥  K♦  9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠
6♦  2♦  J♦  J♠  A♠  2♠  2♣  J♥  7♥  3♠  8♦  10♥  4♦
K♠  8♠  Q♠  5♦  8♥  A♥  A♦  9♠  10♦  Q♣  5♠  4♠  9♦
Q♦  K♣  7♣  10♠  3♦

18 Player 2: 4♥
Pile(1)
4♥

Hand1(8)
K♥  4♣  8♣  5♣  9♣  Q♥  3♣  5♥

Hand2(43)
3♥  K♦  9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦
2♦  J♦  J♠  A♠  2♠  2♣  J♥  7♥  3♠  8♦  10♥  4♦  K♠
8♠  Q♠  5♦  8♥  A♥  A♦  9♠  10♦  Q♣  5♠  4♠  9♦  Q♦
K♣  7♣  10♠  3♦

19 Player 1: K♥
Cost is 3, Player 2 paying 3♥
Cost is 3, Player 2 paying K♦
Cost is 3, Player 1 paying 4♣
Cost is 3, Player 1 paying 8♣
Cost is 3, Player 1 paying 5♣
Turn winner is player 2
Hand1(4)
9♣  Q♥  3♣  5♥

Hand2(48)
9♥  6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦
J♠  A♠  2♠  2♣  J♥  7♥  3♠  8♦  10♥  4♦  K♠  8♠  Q♠
5♦  8♥  A♥  A♦  9♠  10♦  Q♣  5♠  4♠  9♦  Q♦  K♣  7♣
10♠  3♦  4♥  K♥  3♥  K♦  4♣  8♣  5♣

20 Player 2: 9♥
Pile(1)
9♥

Hand1(4)
9♣  Q♥  3♣  5♥

Hand2(47)
6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠
A♠  2♠  2♣  J♥  7♥  3♠  8♦  10♥  4♦  K♠  8♠  Q♠  5♦
8♥  A♥  A♦  9♠  10♦  Q♣  5♠  4♠  9♦  Q♦  K♣  7♣  10♠
3♦  4♥  K♥  3♥  K♦  4♣  8♣  5♣

21 Player 1: 9♣
Pile(2)
9♥  9♣

Hand1(3)
Q♥  3♣  5♥

Hand2(47)
6♥  10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠
A♠  2♠  2♣  J♥  7♥  3♠  8♦  10♥  4♦  K♠  8♠  Q♠  5♦
8♥  A♥  A♦  9♠  10♦  Q♣  5♠  4♠  9♦  Q♦  K♣  7♣  10♠
3♦  4♥  K♥  3♥  K♦  4♣  8♣  5♣

22 Player 2: 6♥
Pile(3)
9♥  9♣  6♥

Hand1(3)
Q♥  3♣  5♥

Hand2(46)
10♣  J♣  A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠  A♠
2♠  2♣  J♥  7♥  3♠  8♦  10♥  4♦  K♠  8♠  Q♠  5♦  8♥
A♥  A♦  9♠  10♦  Q♣  5♠  4♠  9♦  Q♦  K♣  7♣  10♠  3♦
4♥  K♥  3♥  K♦  4♣  8♣  5♣

23 Player 1: Q♥
Cost is 2, Player 2 paying 10♣
Cost is 2, Player 2 paying J♣
Cost is 1, Player 1 paying 3♣
Turn winner is player 2
Hand1(1)
5♥

Hand2(51)
A♣  2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠  A♠  2♠  2♣
J♥  7♥  3♠  8♦  10♥  4♦  K♠  8♠  Q♠  5♦  8♥  A♥  A♦
9♠  10♦  Q♣  5♠  4♠  9♦  Q♦  K♣  7♣  10♠  3♦  4♥  K♥
3♥  K♦  4♣  8♣  5♣  9♥  9♣  6♥  Q♥  10♣  J♣  3♣

24 Player 2: A♣
Cost is 4, Player 1 paying 5♥
Hand1(0)


Hand2(50)
2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠  A♠  2♠  2♣  J♥
7♥  3♠  8♦  10♥  4♦  K♠  8♠  Q♠  5♦  8♥  A♥  A♦  9♠
10♦  Q♣  5♠  4♠  9♦  Q♦  K♣  7♣  10♠  3♦  4♥  K♥  3♥
K♦  4♣  8♣  5♣  9♥  9♣  6♥  Q♥  10♣  J♣  3♣

Game over! Winner is player 1
Pile(2)
A♣  5♥

Hand1(0)


Hand2(50)
2♥  6♠  7♦  6♣  7♠  6♦  2♦  J♦  J♠  A♠  2♠  2♣  J♥
7♥  3♠  8♦  10♥  4♦  K♠  8♠  Q♠  5♦  8♥  A♥  A♦  9♠
10♦  Q♣  5♠  4♠  9♦  Q♦  K♣  7♣  10♠  3♦  4♥  K♥  3♥
K♦  4♣  8♣  5♣  9♥  9♣  6♥  Q♥  10♣  J♣  3♣

25 turns, longest penalty run 6
$
```
