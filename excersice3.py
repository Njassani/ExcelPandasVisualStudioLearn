import pandas as pd 
# Read Excel
df=pd.read_excel('modified.xls')

#Add Rate Column
df['Rate%']= df['Pay'].apply (lambda x: 0 if x<10000 else 0.15 if 10000<x<40000 else 0.20 if 40000<x<80000 else 0.25)
#Add Tax Column
df['Tax']= df['Pay']*df['Rate%']
#Delete Zipcode, First, Address Columns
to_drop=['Zipcode','First', 'Address']
df.drop(columns=to_drop, inplace=True)

#Saving in a new version file
df.to_excel('modified2.xlsx')
df=pd.read_excel('modified2.xlsx')

#troubleshooting for dropping the Unnamed columns
to_drop=['Unnamed: 0','Unnamed: 0.1']
df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
#resaving the excel file
df.to_excel('modified3.xlsx')
df=pd.read_excel('modified3.xlsx')
#renaming column 1
df.columns= ['Record#','Last', 'City', 'State', 'Pay', 'Rate%', 'Tax']
print(list(df))

