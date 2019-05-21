# pycompseries

This library can compare two series of outcomes and declare the winner series with better outcome. Tricky part is, that it will declare as winner only 'clear winner' - meaning series needs to have better outcome on vast majority of indexes, but not necessary on all of them. In another words, library is simple Stochastic-based comparator of two series - with fixed and unknown (but consistent) behaviour. It is responsibility of the client to judge its usability and backtest it with relation to its usage.

## General Idea

Let A and B be series of lenght I. Lets create N random trees T with random values. Let A and B play game G using trees T as playing ground. Winner is declared only if either A or B wins all games.

Game G:
  Player (A or B) can choose its move if value of outcome on current index I is bigger than opponents one. Player with more points at the and of the round is winner. (of the round, there should be many rounds on different trees). Player should walk the path by using minimax search (with assumption that moves will change evenly).

Tree T:
  Tree can should bottlenecked every time it reaches certain modulo depth by having there only one vertex.

## Authors

* **mcXrd** - *Initial work*
