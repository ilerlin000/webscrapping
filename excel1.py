import openpyxl as xl
from openpyxl.styles import Font

# Create a new excel document
wb = xl.Workbook()

# Assign the current sheet to the 'MySheet' worksheet object variable
MySheet = wb.active

# Rename the name of the sheet 
MySheet.title = 'First Sheet'

# Create a new worksheet
wb.create_sheet(index=1,title='Second Sheet')

# Write content to a cell
MySheet['A1'] = 'An Example of Sum Formula'

# Change the font size and italicize
MySheet['A1'].font = Font(name='Times New Roman',size=24,italic=True, bold=True)

# Alternatively you can create a Font object and assign it
fontobject = Font(name='Times New Roman',size=24,italic=True, bold=True)

MySheet['A1'].font = fontobject

# Adding value to cells
MySheet['B2'] = 50
MySheet['B3'] = 75
MySheet['B4'] = 100


MySheet['A5'] = 'Total'
MySheet['A5'].font = Font(size=16,bold=True)

MySheet['B5'] = '=SUM(B2:B4)'

# Change the column width
MySheet.column_dimensions['A'].width = 25




wb.save('PythonToExcel.xlsx')