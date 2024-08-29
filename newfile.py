import pandas as pd
TurbineData=pd.read_csv('Turbine_Data.csv')
Turbine_df=pd.DataFrame(TurbineData)
Turbine_df.dropna()
df=Turbine_df.WindSpeed<3
Turbine_df.drop(Turbine_df.WindSpeed<3,axis=1)




