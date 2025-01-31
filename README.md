filterset_fields = {
        "user__name": ["exact", "icontains"],
        "created_at": ["date__gte", "date__lte"],
        "specialization": ["exact"],
    }


# Big O Notation O(n)

Big O Notation is used to measure how running time or space requirements for your program grow as 
input size grows.

time = a*n + b where b is constant
(1) Keep the fastest growing terms
    time = a * n
(2) Drop Constants
    time = O(n)

Big O refers to very large number of n.
    time = 5 * n² + 3 * n + 20
when value of n is very large 3 * n + 20 becomes irrelevant.

Measuring running time growth: time complexity
Measuring space growth: space complexity

Binary Search Iteration k = n/2^k 


# Advantages of linked list over arrays

https://www.prepbytes.com/blog/linked-list/advantage-and-disadvantage-of-linked-list-over-array/
