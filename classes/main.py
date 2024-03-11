# 10.1
class Thing():
  pass
print(Thing)
example = Thing()
print(example)
# 10.2
class Thing2():
  letters = 'abc'
print(Thing2().letters)
# 10.3
class Thing3():
  def __init__(self):
    self.letters = 'xyz'
print(Thing3().letters)
# 10.4
class Element():
  def __init__(self, name, symbol, number):
    self.name = name
    self.symbol = symbol
    self.number = number
print(Element('Hydrogen', 'H', 1))
# 10.5
el_dict = {
  'name': 'Hydrogen',
  'symbol': 'H',
  'number': 1
}
hydrogen = Element(**el_dict)
print(hydrogen.name)
# 10.6
class Element():
  def __init__(self, name, symbol, number):
    self.name = name
    self.symbol = symbol
    self.number = number
  def dump(self):
    return f'name={self.name}, symbol={self.symbol}, number={self.number}'
hydrogen = Element(**el_dict)
print(hydrogen.dump())
# 10.7
print(hydrogen)
class Element():
  def __init__(self, name, symbol, number):
    self.name = name
    self.symbol = symbol
    self.number = number
  def __str__(self):
    return f'name={self.name}, symbol={self.symbol}, number={self.number}'
hydrogen = Element(**el_dict)
print(hydrogen)
# 10.8
class Element():
  def __init__(self, name, symbol, number):
    self.__name = name
    self.__symbol = symbol
    self.__number = number
  def __str__(self):
    return f'name={self.name}, symbol={self.symbol}, number={self.number}'
  @property
  def name(self):
    return self.__name
  @property
  def symbol(self):
    return self.__symbol
  @property
  def number(self):
    return self.__number
hydrogen = Element(**el_dict)
print(hydrogen.name)
# 10.9
class Bear():
  def eats(self):
    return 'berries'
class Rabbit():
  def eats(self):
    return 'clover'
class Octothorpe():
  def eats(self):
    return 'campers'

bear = Bear()
print(bear.eats())
rabbit = Rabbit()
print(rabbit.eats())
octothorpe = Octothorpe()
print(octothorpe.eats())