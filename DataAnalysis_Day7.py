#DataFrame
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint

import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
#webbrowser.open(website)

nfl_frame = pd.read_clipboard()
pprint(nfl_frame)

print("\n\nName of all columns in DF:\n{}".format(nfl_frame.columns))
print("\n\nRows under column Team :\n{}".format(nfl_frame.Team))
print("\n\nRows under column NFL:\n{}".format(nfl_frame['NFL']))
print("\n\nPandas fills NaN for column name that does not originally exist:\n{}".format(DataFrame(nfl_frame,columns=['Team','Won','Lost','Stadium'])))

print("\n\nRetrieve first 2 rows:\n{}".format(nfl_frame.head(2)))

print("\n\nRetrieve last 2 rows:\n{}".format(nfl_frame.tail(2)))

print("\n\nFind out all columns on particular row\n{}".format(nfl_frame.iloc[3]))
#use iloc when it is an integer and loc when it is a label

nfl_frame['Stadium'] = "Levi's Stadium"
print("\n\nAssigning a value to new column Stadium \n")
pprint(nfl_frame)
nfl_frame['Stadium']=np.arange(6)
print("\n\nAssigning 0-6 to new column stadium:\n")
pprint(nfl_frame)

stadiums = Series(["Levi's Stadium","AT&T Stadium"],index = [5,0])
#print(stadiums)
nfl_frame['Stadium'] = stadiums
print("\n\nAssigning series value to new column stadium:\n{}".format(nfl_frame))

del nfl_frame['Stadium']
print(nfl_frame)

data = {'City':['SF','LA','NYC'],'Population':[837000,3880000,8400000]}
city_frame = DataFrame(data)
print("\n\nConstructing DF from dictionaries:\n{}".format(city_frame))
