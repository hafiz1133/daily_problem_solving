# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
def find_uniq(arr):
    for i in range(len(arr)):
        if arr[i]==arr[i+1]:
            pass
        else:
            try:
                if arr[i+1]==arr[i+2]:

                    return(arr[i])
                else:
                    return(arr[i+1])
                break
            except:
                return(arr[i+1])
                break
#others Solutins
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e
# another
def find_uniq(arr):
    arr.sort()
    return arr[0] if arr[0] != arr[1] else arr[-1]