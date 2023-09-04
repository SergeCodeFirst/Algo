



# # Find the sum of each sub array of length k
# def sum_subarray(arr, k):
#     sum_curret_sub = sum(arr[:k])
#     result = [sum_curret_sub]

#     for i in range(1, (len(arr)-k + 1)):
#         sum_curret_sub = sum_curret_sub - arr[i -1]
#         sum_curret_sub = sum_curret_sub + arr[i+ k-1]

#         result.append(sum_curret_sub)
    
#     return result

# print(sum_subarray([1,2,3,4,5,6,7,8,9], 3))


# Find the min lenght of a sub array that sum up to x

def min_Sub_arr_len(arr, x):
    min_len = float('inf')
    cur_sum = 0
    start = 0
    end = 0

    for i in range(len(arr)):
        cur_sum += arr[i]
        end += 1

        while start< end and cur_sum >= 7:
            min_len = min(min_len, len(arr[start:end]))
            
            cur_sum -= arr[start]
            start += 1

    return min_len




print(min_Sub_arr_len([1,2,3,4,5,6], 7))