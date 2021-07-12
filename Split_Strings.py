# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    main_ls = []
    ln = len(s)
    if ln % 2 == 0:
        for i in range(ln):
            if i % 2 != 0:
                inside_list = s[i - 1] + s[i]
                main_ls.append(inside_list)

    else:
        s = s + '_'
        for i in range(ln + 1):
            if i % 2 != 0:
                inside_list = s[i - 1] + s[i]
                main_ls.append(inside_list)
    return main_ls