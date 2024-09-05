import pandas as pd
TurbineData=pd.read_csv('Turbine_Data.csv')
Turbine_df =pd.DataFrame(TurbineData)
df=Turbine_df.isna().sum()
Turbine_df=Turbine_df.dropna()
Turbine_df.isna().sum()
Turbine_df['ActivePower']= [ value  if value>0 else 0 for value in Turbine_df['ActivePower'] ]        





 




