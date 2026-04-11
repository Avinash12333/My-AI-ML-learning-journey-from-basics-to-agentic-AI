# Exercise 1
# Given a list of numbers, return only the unique ones, sorted
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 2]
result = sorted(set(numbers))
print(result)


# Exercise 2
# Count word frequency in this sentence using a dict
sentence = "the cat sat on the mat the cat"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
# Output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# Exercise 3
# Given two lists, return elements that appear in both
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)
print(common)
# Output: {3, 4, 5}

# Exercise 4
# Unpack list of tuples into two separate lists
students = [("Avinash", 95), ("John", 87), ("Sara", 92)]
names = [s[0] for s in students]
scores = [s[1] for s in students]
print(names)
print(scores)
# Output: ['Avinash', 'John', 'Sara']
# Output: [95, 87, 92]

# Exercise 5
# Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sublist in nested for x in sublist]
print(flat)
# Output: [1, 2, 3, 4, 5, 6]