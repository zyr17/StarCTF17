; Machine starts in state 0.

0 F _ r 0.1
0.1 D _ r 0.2
0.2 U _ r 0.3
0.3 C _ r 0.4
0.4 T _ r 1
0.4 * * * reject

1 F _ r 1.1
1.1 { _ r 2
1.1 * * * reject

2 } _ * 3 
2 * * r 2

3 * * l 4

4 R _ l 5
5 5 _ l 6
6 3 _ l 7
7 P _ l 8
8 t _ l 9
9 0 _ * 10
9 * * * reject


10 _ _ l 10.1
10.1 N  * l 10.2
10.2 e * l 10.3
10.3 L * l 10.4
10.4 p * l 10.5
10.5 P * l 10.6
10.6 4 * l 10.7
10.7 _ _ r 11
10.7 * * * reject

11 4 _ r 12
12 P _ r 13
13 p _ r 14
14 L _ r 15
15 e _ r 16
16 N _ r accept
16 * * * reject

accept * * r halt-accept
reject * * r halt-reject