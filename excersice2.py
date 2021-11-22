import pandas as pd 
df=pd.read_csv('Names.csv', header=None)
df.columns= ['First', 'Last', 'Address', 'City', 'State','ZipCode', 'Pay']
df['Rate%']= df['Pay'].apply (lambda x: 0 if x<10000 else 0.15 if 10000<x<40000 else 0.20 if 40000<x<80000 else 0.25)
df['Tax']= df['Pay']*df['Rate%']
to_drop=['ZipCode', 'First', 'Address']
df.drop(columns=to_drop, inplace=True)
print(df)
df.to_csv('modified.csv')