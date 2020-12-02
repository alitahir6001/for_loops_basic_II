# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie(arr):
    for i in range(len(arr)):
        if arr[i] >= 0: 
            arr[i] = "big"
    return arr
    print(arr)
sizeme = [-1,3,5,-5] # created a second var to hold the array values to bypass "typeError" message
print(biggie(sizeme))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def positives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    arr[-1] = count
    return arr
print(positives([-1,1,1,1,3]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def totalsum(arr):
    count = 0
    for i in range(len(arr)):
        count = count + arr[i]
    return count
print(totalsum([1,2,3,4]))
print(totalsum([-2,8,6,-5]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def Average(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum / len(arr) # used modulo first, but that's not what i want here cuz it'll return the whole number, and i want the decimal place included.
print(Average([1,2,3,4]))
print(int(Average([1,2,3,4]))) # was curious to see how i could get rid of the deicmal and use whole numbers only, so i looked up 'removing decimals python' and used int(), and also could've used math.trunc()

# Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(arr):
    return len(arr) # I can't seem to wrap this in a print statement, and just call the function later.
print(length([1,2,3,4,5,6,7,8,9]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def mini(arr):
    min = arr[0]
    if len(arr) == 0:
        return False
    for i in arr: 
        if i < min:
            min = i
    return min
print(mini([37,2,1,-9]))
print(mini([]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maxi(arr):
    max = arr[0]
    if len(arr) == 0:
        return False
    for i in arr: 
        if i > max:
            max = i
    return max
print(maxi([37,2,1,-9]))
print(maxi([]))  # I basically copied the minimum function and changed did some small edits to change the var min to max, and at line 81 changed < to >. I keep getting an "indexError" for the empty array saying the list is out of range..


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate(arr):
    def ultimate_analyze(arr):
        dict = {  #dictionaries use curly braces, not square brackets
            'sumtotal' : sum(arr),
            'average' : average(arr),
            'minimum' : minimum(arr),
            'maximum' : maximum(arr),
            'length' : len(arr)
            }
    return dict
print(ultimate([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def backwards(arr):
    arr = reverse(arr)
    return arr
print(backwards([37,2,1,-9]))

#these last two were challenging. I basically used my assignments from Basic Foundations I and II to follow my logic i used there but I'm still having trouble with the syntax.