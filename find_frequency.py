def find_frequency(s):
    frequency = {}
    for char in s :
        frequency[char] = frequency.get(char, 0 ) +1
    return frequency
a= find_frequency("Samuel david")
print(a)