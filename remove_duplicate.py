import pandas as pd 
import numpy as np 
import datetime
data = pd.read_csv("/home/xsalassa/hackathon/NIK with all color/NIK with Various Color Status.csv")
from datetime import datetime

data['checkin_timestamp'] = pd.to_datetime(data['checkin_timestamp']).dt.date

print(data)
data1  =data.drop_duplicates(subset=["nik_hashed","checkin_timestamp", "outlet_sub_category"], keep='first' )
print(data1)
print(data1['nik_hashed'].nunique)

data1.to_csv('mix_new.csv')