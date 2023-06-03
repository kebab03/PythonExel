# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Mac")
import pandas as pd

data = [['June', 1837],
        ['May', 1885],
        ['April', 2010],
        ['March', 1859],
        ['February', 1494],
        ['January', 1704],
        ['December', 1630],
        ['November', 1553],
        ['October', 1646],
        ['September', 1726],
        ['August', 1810],
        ['July', 1871]]

df = pd.DataFrame(data, columns=['Month', 'Income'])
df.to_csv('file.csv', index=False)
