import pandas as pd

data = pd.read_excel("database.xls")

# The data variable now contains a pandas DataFrame with the contents of the .ods file.
print(type(data))
print(data.keys())
data = data.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# print the result
print(data)
data.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')