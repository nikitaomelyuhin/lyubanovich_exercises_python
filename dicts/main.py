# 8.1
e2f = { 
  'dog': 'chien',
  'cat': 'chat',
  'walrus': 'morse',
}
print(e2f)
# 8.2
print(e2f['walrus'])
# 8.3
f2e = {}
for key, value in e2f.items():
  f2e[value] = key
print(f2e)
# 8.4
print(f2e['chien'])
# 8.5
print(set(e2f.keys()))
# 8.6
life = {
  'animals': { 
    'cats': ['Henri', 'Grumpy', 'Lucy'],
    'octipi': {},
    'emus': {}
  },
  'plants': {},
  'other': {}
}
# 8.7
print(life.keys())
# 8.8
print(life['animals'].keys())
# 8.9
print(life['animals']['cats'])
# 8.10
squares = dict()
for num in range(10):
  squares[num] = num ** 2
print(squares)
# 8.11
odd = set(num for num in range(10) if num % 2 != 0)
print(odd)
# 8.12
for thing in (f'Got {number}' for number in range(10)):
  print(thing)
# 8.13
tuple_1 = ('optimist', 'pessimist', 'troll')
tuple_2 = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
tuple_res = {}
for tuple_1_value, tuple_2_value in zip(tuple_1, tuple_2):
  tuple_res[tuple_1_value] = tuple_2_value
print(tuple_res)

# 8.14
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks Ona Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
movies = {}
for title, plot in zip(titles, plots):
  movies[title] = plot
print(movies)

# Из учебника
# keys = ('optimist', 'pessimist', 'troll')
# values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
# dict(zip(keys, values))
