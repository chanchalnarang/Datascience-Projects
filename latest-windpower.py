import pandas as pd
TurbineData=pd.read_csv('Turbine_Data.csv')
Turbine_df =pd.DataFrame(TurbineData)
df=Turbine_df.isna().sum()
Turbine_df=Turbine_df.dropna()
Turbine_df.isna().sum()
Turbine_df['ActivePower']= [ value  if value>0 else 0 for value in Turbine_df['ActivePower'] ]
print(Turbine_df)


# CleanData=Turbine_df 
# Clean_df=pd.DataFrame(CleanData)
# Clean_df_updated=[pd.to_datetime(row) for row in Clean_df['Unnamed: 0']]
# updated_Df=pd.DataFrame(Clean_df_updated)
# print(updated_





 




