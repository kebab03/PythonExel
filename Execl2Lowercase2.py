import odfpy

import pandas as pd

#data = pd.read_excel("Data.ods")
data = pd.read_excel("Data.ods", engine="odf")
# The data variable now contains a pandas DataFrame with the contents of the .ods file.
print(type(data))
print(data.keys())

data = data.applymap(lambda x: x.lower() if isinstance(x, str) else x)
data['Cognome'] = data['Cognome'].apply(lambda x: x.lower() if isinstance(x, str) else x)
# print the result
print(data)
data.to_excel('pandas_excel.xlsx', sheet_name='new_sheet_name')