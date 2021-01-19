'''
   Notes

   from NZ whiteboard sess.



1) Chiara:
   First n Fibonnaci numbers

   askk

   0 1 1 2 3 5


2) A and B, sorted, B has one element missing from A


   for i in range(A):
       if A[i] != B[i]:
           return A[i]

---


'''


def fib(n):
    """
    n : int nth number
    """

    f0 = 0
    f1 = 1

    if n == 0:
        f = f0
    elif n == 1:
        f = f1
    else:

        fprev_0 = f0
        fprev_1 = f1
        for i in range(n-2):
            f       = fprev_1 + fprev_0
            fprev_0 = fprev_1
            fprev_1 = f

    return f




def fibrec(n):
    """
    Recursive. Better.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibrec(n-1) + fibrec(n-2)
