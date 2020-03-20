'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#plan
#
#go through each letter to find "th"
#recursively should occur when counting th
#base case should be if len is < 2
def count_th(word):
   #base case
    if(len(word)< 2):
        return 0
    #check the first two letters for th and then call the function again but with one letter ahead and return 1
    if(word[:2] == "th"):
        return 1 + count_th(word[1:])
    #when not found call the function again but with one letter ahead
    else:
        return count_th(word[1:])
print(count_th("oefwawthafwethaes"))
