# -*- coding: utf-8 -*-
"""
Created on Fri May 27 21:08:36 2022
@author: Mohammed Ibrahim Abdelmonem            Sec:3    
"""
def can_All_Vote(arr, n, x):
 
    # calculate total sum of time taken by all people
    total_sum = 0
    for i in range(len(arr)):
        total_sum += arr[i]
    #print(total_sum)   
    # if total time is less than x then all people can definitely vote hence return true
    if(total_sum <= x):
        return True
     
    # sort the list
    arr.sort()
    #print(arr) 
    # declare a list presum of same size as that of arr and initialize it with 0
    pre_sum = [0 for i in range(len(arr))]
 
    # prefixsum for first element will be element itself
    pre_sum[0] = arr[0]
     
    # fill the array
    for i in range(1, len(pre_sum)):
        pre_sum[i] = pre_sum[i - 1] + arr[i]
     
    # Set i and j and check if array
    # from i to j - 1 gives sum <= x
    for i in range(0, len(pre_sum)):
        for j in range(i + 1, len(pre_sum)):
            arr1_sum = (pre_sum[i] + (total_sum - pre_sum[j]))
            if((arr1_sum <= x) and
               (total_sum - arr1_sum) <= x):
                return True
     
    return False

# Driver code
limit_Time = 9 # maximum time for every machine to be operational
#looping for rounds voting and callin method to see results
# The time spent by each person    
Time_per_person = [[2, 5, 2 ,2 ,3 ,1 ,1],
        [2, 5, 2 ,2 ,3 ,1 ,1 ,2 ,3,3] ,
        [2, 4, 3 ,5 ,4]]
# number of persons will voting consider as (n)
n = [7,10,5]
for i in range(0 ,3):
    if(can_All_Vote(Time_per_person[i], n[i], limit_Time )):
        print("YES all people can vote in round {n}".format(n=i+1))
    else:
        print("All people can't vote in round {n}".format(n=i+1))    