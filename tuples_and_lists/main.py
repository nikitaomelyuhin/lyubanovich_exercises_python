# 7.1
years_list = [1994, 1995, 1996, 1997, 1998]
# 7.2
third_birthday = years_list[3]
# 7.3
most_years = years_list[-1]

print(third_birthday, most_years)

# 7.4
things = ['mozzarella', 'cinderella', 'salmonella']
# 7.5
things[1] = things[1].capitalize()
print(things)
# 7.6
things[0] = things[0].upper()
print(things)
# 7.7
del things[2]
print(things)
# 7.8
surprise = ['Groucho', 'Chico', 'Harpo']
# 7.9
surprise[-1] = surprise[-1].lower()

last_surprise_array_inverse = []

for letter in surprise[-1]:
  last_surprise_array_inverse.insert(0, letter)
  
last_inverse = ''.join(last_surprise_array_inverse).capitalize()

print(last_inverse)

# ``` Из учебника
# >>> surprise[-1] = surprise[-1].lower()
# >>> surprise[-1] = surprise[-1][::-1]
# >>> surprise[-1].capitalize()
# ```

# 7.10
even = [num for num in range(10) if num % 2 == 0]
print(even)
# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

start1_caps = " ".join([word.capitalize() + "!" for word in start1])

for first, second in rhymes:
    print(f"{start1_caps} {first.capitalize()}!")
    print(f"{start2} {second}")
