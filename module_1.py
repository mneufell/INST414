from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#Create the data frame from the CSV
data = pd.read_csv("states.csv")
#Filtering out the M names from the data frame
filter_out_m = data['Sex'] == 'F'
#reassigning data to not include M names 
data =data[filter_out_m]
#Changing the year column from STR to INT
data['Year'] = data['Year'].astype(int)
#filtering the out years before 2021
filter_year = data['Year'] >=2021
#reassigning data to not include years before 2021
data = data[filter_year]
#drops columns Total and Count_Normalized
data = data.drop(columns=['Total', 'Count_Normalized']) 
#filtering to have the output of the top 5 names in MD
filter_states_md = (data['State'] =='MD') & (data['Count']>=218)
#filtering to have the output of the top 5 names in CA
filter_state_ca = (data['State'] == 'CA') & (data['Count'] > 1800)
#reassigning data to only the top 5 names in MD
data_md=data[filter_states_md]
#reassigning data to only the top 5 names in CA
data_ca = data[filter_state_ca]
#combining both datasets into one
df = pd.concat([data_md, data_ca], axis=0)
#creating graph of the top 5 names in both MD and CA
pd.crosstab(df['Name'], df['State'], values = df['Count'], aggfunc='sum').plot(kind='bar')
plt.show()