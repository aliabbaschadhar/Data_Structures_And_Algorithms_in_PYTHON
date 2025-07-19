# Find the frequency of number in a list using dictionary?

nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]

freq = {}
hash = dict()
x = 1

# Brute force method
for i in range(0, len(nums)):
    if nums[i] in freq:
        freq[nums[i]] += 1
    else:
        freq[nums[i]] = 1

print("Brute Force \n", freq)

# Hashing method shortcut
for i in range(0, len(nums)):
    hash[nums[i]] = hash.get(nums[i], 0) + 1

print("Hashing method: ", hash)

if x in freq:
    print(freq[x])
