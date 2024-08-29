import pandas as pd
from pandas import DatetimeIndex
TurbineData=pd.read_csv('Turbine_Data.csv')
Df=pd.DataFrame(TurbineData)
Df1=Df.dropna()
Df1.columns.name=[ 'Index','Timestamp' ]
print(Df1)
#Data_Array=pd.DatetimeIndex(Data_Array,dayfirst=True)
#df=pd.DataFrame(Data_Array)
#print(df)
#Transforming timestamp to date and time

#Turbine_df.dropna()
#df=Turbine_df.WindSpeed<3
#Turbine_df.drop(Turbine_df.WindSpeed<3,axis=1)




