# Solving Assignment Problem with Auction Algorithm
### Shimeng Wang, Zhining Chen
## Problem Description
There are now $N$ patients and $K$ doctors. Each patient has a prefered list of doctors. For doctor %j%, his capacity for patients is $C_j$, and $\sum C_j > N$. The goal is to find an optimal assignment of doctors to patients. 
## The classical assignment problem
The classical assignment problem has $N$ people and $N$ objects, and we need to match each person to an object based on their preference. Particularly, the value of object $j$ to person $i$ is denoted $a_{ij}$, and we want to optimize $max{\sum a_{ij}}$. Bertsekas 1988 proved that classical assignemnt problem can be solved with auction algorithm in limited auction rounds. For our problem the number of objects and people are different, but it can be transformed into the classical problem by treating each available spot of doctors to an unique object and assume there are some low priority patient to fill the gap between number of objects and people.
## Auction process
In our scenario, each patient has a ranked preference for doctors. If a patient prefers a doctor, then his rating for this doctor is higher. Connecting to the auction algorithm, we define the ratings to be how much this patient would pay for each doctor.We also define that the available spot{j} has a market price $p_j$ that every patient can bid on. Therefore, the profit for spot $j$ to patient $i$ is $a_{ij}-p_{j}$. We call a patient{i} is happy if $a_{i{j_i}}-p_{j_i}\leq max{a_{ij}-p_{j}-\epsilon}$ where $j_i$ is the spot currently assigned to patient$i$ and $\epsilon$ is the small service fee in each round of bid. Namely, a patient is happy if he is assigned the largest profit spot.

At the beginning, each patient is assigned to a spot randomly. If every patient is happy, the auction ends, and we already found the optimal assignment plan. If patient $i$ is not happy, he would bid for the spot he can make the most profit. The money he would like to add to the price is the difference between the largest spot profit and the second largest spot profit minus the service fee $\epsilon$. Namely he set the price of his most desired spot $j_i$ from $p_{j_i}$ to $p_{j_i}+(\max\limits_j{a_{ij}-p_{j}}-\max\limits_{j\neq j_i}{a_{ij}-p_{j}})+\epsilon$.

## Termination
The auction process will terminate in finite number of rounds. Once a patient has bid for a spot, he would not voluntarily give up the spot because the price of other spots only increase and thus his spot remains the largest profit to him. He would only lost his spot if someone has bid for it with a higher price. Thus he would only receive a spot that has never been bid before. If all spots have been bid, then the auction ends. Also notice in each round of auction, the price increase with a minimum of $\epsilon$. For sufficiently large rounds of bid, the spot should be expensive enough, which makes those never bid spot most profitable to some patients. Thus all spots will receive at least one bid, and the auction will terminate eventually.

## Time Complexity and Optimality
Optimality of auction algorithm is garenteed as long as $n\epsilon \le 1$. Particularly out assignment is within $n\epsilon$ of being optimal. As every doctor-to-patient value $a_{ij}$ is integer, thus it garentees the optimal assignment result. 


$\epsilon$ determines the converging speed of the auction process. Let $C$ denote the maximum of $a_{ij}$, and the running time should be $\mathcal{O}(\frac{C}{\epsilon})$. Since both $C$ and $\frac{1}{\epsilon}$ is $\mathcal{O}(N)$, the time frequency should be $\mathcal{O}(N^2)$.

## Citation
Bertsekas, Dimitri P. "The auction algorithm: A distributed relaxation method for the assignment problem." Annals of operations research 14.1 (1988): 105-123.