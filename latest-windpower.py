
import pandas as pd
import numpy as np
from pandas import DatetimeIndex
TurbineData=pd.read_csv('Turbine_Data.csv')
Turbine_df =pd.DataFrame(TurbineData)
df=Turbine_df.isna().sum()
Turbine_df=Turbine_df.dropna()
df1=Turbine_df.isna().sum()
CleanData=Turbine_df 
Clean_df=pd.DataFrame(CleanData)
print(Clean_df.isna().sum())
print(Clean_df)
