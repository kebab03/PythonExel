import subprocess

# Define the days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Define the starting cell for the week
start_cell = 'A1'

# Define the number of days in the week
num_days = len(days_of_week)

# Define the ending cell for the week
end_cell = f'{chr(ord(start_cell[0]) + num_days - 1)}{int(start_cell[1:])}'

# Construct the data string for the week
data = '\t'.join(days_of_week)

# Open LibreOffice Calc and create a new document
subprocess.call(['C:\\Program Files\\LibreOffice\\program\\soffice.exe', '--calc'])

# Set the cell range to the starting and ending cells for the week
subprocess.call(['unoconv', '--format=xls', f'--sheet="Sheet1" --range={start_cell}:{end_cell}', '-'])

# Paste the week data into the selected cells
subprocess.call(['xsel', '--input'], input=data.encode())
subprocess.call(['xsel', '--output', '--paste'])
subprocess.call(['xdotool', 'key', 'ctrl+v'])
