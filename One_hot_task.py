import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'WhoAmI':lst})
# data.head()
headers = set(lst)
data_dict = {}
for el in headers:
  data_dict[el] = [1 if el == elm else 0 for elm in lst]
result = pd.DataFrame(data_dict)
result