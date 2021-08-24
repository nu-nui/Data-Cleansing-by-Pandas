# Sales csv file is showing all column type as object.
# I need to correct it by below code.
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/FileName.csv', encoding = "ISO-8859-1")
df['TYPE'] = df['TYPE'].astype('string')
df['BOI TYPE'] = df['BOI TYPE'].astype('string')
df['Month'] = df['Month'].astype('string')
df['INVOICE NO.'] = df['INVOICE NO.'].astype('string')
df['CUSTOMER'] = df['CUSTOMER'].astype('string')
df['CUSTOMER1'] = df['CUSTOMER'].astype('string')
df['CATEGORY'] = df['CATEGORY'].astype('string')
df['CATEGORY1'] = df['CATEGORY1'].astype('string')
df['P/O NO.'] = df['P/O NO.'].astype('string')
df['ITEM CODE'] = df['ITEM CODE'].astype('string')
df['DESCRIPTION'] = df['DESCRIPTION'].astype('string')
df['UOM'] = df['UOM'].astype('string')
df['DESCRIPTION'] = df['DESCRIPTION'].astype('string')
df = df.drop('Unnamed: 17', axis=1)
df['QUANTITY'] = df['QUANTITY'].astype('str')
df['AMOUNT'] = df['AMOUNT'].astype('str')

# Some column can't convert type to numeric. Clean it!!
def convert_ft(val):
    new_val = val.replace(',' , '')    
    return float(new_val)
  
df['QUANTITY'] = df['QUANTITY'].apply(convert_ft)
df['UNIT PRICE'] = df['UNIT PRICE'].apply(convert_ft)
df['AMOUNT'] = df['AMOUNT'].apply(convert_ft)

# In column DATE, I want to show only date.
df['DATE'] = pd.to_datetime(df['DATE']).dt.strftime('%d')

df.to_csv('FinalFile.csv', index=False)