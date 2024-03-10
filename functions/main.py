# 9.1
def good():
  return ['Harry', 'Ron', 'Hermione']
print(good())
# 9.2
def get_odds():
  for number in range(1, 10, 2):
    yield number

count = 1
for number in get_odds():
  if count == 3:
    print("The third odd number is", number)
    break

  count += 1
print(get_odds())
# 9.3
def test(func):
  def new_func(*args, **kwargs):
    print('start')
    result = func(*args, **kwargs)
    print('end')
    return result
  return new_func
# 9.4
class OopsException(Exception):
  pass

try:
  raise OopsException
except OopsException:
  print('Caught an oops')