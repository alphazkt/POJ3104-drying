# POJ3104-drying
It is very hard to wash and especially to dry clothes in winter. But Jane is a very smart girl. She is not afraid of this boring process. Jane has decided to use a radiator to make drying faster. But the radiator is small, so it can hold only one thing at a time.

Jane wants to perform drying in the minimal possible time. She asked you to write a program that will calculate the minimal time for a given set of clothes.

There are n clothes Jane has just washed. Each of them took ai water during washing. Every minute the amount of water contained in each thing decreases by one (of course, only if the thing is not completely dry yet). When amount of water contained becomes zero the cloth becomes dry and is ready to be packed.

Every minute Jane can select one thing to dry on the radiator. The radiator is very hot, so the amount of water in this thing decreases by k this minute (but not less than zero — if the thing contains less than k water, the resulting amount of water will be zero).

The task is to minimize the total time of drying by means of using the radiator effectively. The drying process ends when all the clothes are dry.

Input

The first line contains a single integer n (1 ≤ n ≤ 100 000). The second line contains ai separated by spaces (1 ≤ ai ≤ 109). The third line contains k (1 ≤ k ≤ 109).

Output

Output a single integer — the minimal possible number of minutes required to dry all clothes.

Sample Input

sample input #1

3

2 3 9

5

sample input #2

3

2 3 6

5

Sample Output

sample output #1

3

sample output #2

2
