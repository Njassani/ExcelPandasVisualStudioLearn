import pandas as pd
import xlr
from openpyxl.workbook import Workbook

df_excel=pd.read_excel('modified.xls')
df_csv= pd.read_csv('Names.csv', header= None)
df_txt =pd.read_csv('data.txt',delimiter='\t')

df_csv.columns= ['First','Last', 'Address', 'City', 'State', 'Zipcode', 'Pay' ]


print(df_excel)