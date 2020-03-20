#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) seams like the runtime would go up a linear amount


b) O(n)^2 nested loop causing it to run longer by a exponential magnitude


c) O(n)It seems like this function only calls the  recursion once per run and the runtime seems to be linear

## Exercise II


#This problem seems to be a binary search type of problem where you are going through the floors and splitting them in half to choose the middle

#1. go through the list of floors and go to the middle to drop the eggs
#2. if it breaks go through the lower half of the list and choose the middle
#3. if the egg doesn't break, do it again but with the top half of the list
#4. the break point will happen when the egg breaks on the higher floor but not the lowe floor

#I think this problem will have a time complexity of O(logn) since we are halfing the inputs