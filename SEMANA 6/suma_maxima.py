
def maximum_subarray(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

S = [-2, 1, -2, 4, -1, 2, 1, -5, 4]
resultado = maximum_subarray(S)

print('*'*20)
print("resultado suma:", resultado)
print('*'*20)
