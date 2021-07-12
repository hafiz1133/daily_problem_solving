# Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.
#
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1)
def is_prime(num):
    flag =True
    if num>1:
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = False
                # break out of loop
                break
        return flag
    else:
        return False
# Others Solutons::
