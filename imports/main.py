# 11.1
import zoo
zoo.hours()
# 11.2
import zoo as managerie
managerie.hours()
# 11.3
from zoo import hours
hours()
# 11.4
from zoo import hours as info
info()
# 11.5
plain = {
  'a': 1,
  'b': 2,
  'c': 3
}
print(plain)
from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
