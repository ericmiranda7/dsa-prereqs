### Decision Decisions
A queue, due to its FIFO nature makes it inefficient to simply dequeue items from the backing array (since we now need to move all the items back one position in order
to save space)  
Thankfully, minds greater than mine have already solved this problem. We have a couple of alternatives -
1. Singly, Doubly Linked Lists
2. Circular Array
I made the decision to go with (2) because linked lists are inefficient and I've already done (or will be doing them) seperately.