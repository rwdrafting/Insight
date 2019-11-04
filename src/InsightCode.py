
import csv
import pandas as pd

#Setting up input and output
Input = 'C:\\Users\\jessw\\Downloads\\border-crossing-analysis-master\\border-crossing-analysis-master\\input\\Border_Crossing_Entry_Data.csv'
Output_path = 'C:\\Users\\jessw\\Downloads\\border-crossing-analysis-master\\border-crossing-analysis-master\\output\\Report.csv'
#reading in data from the specified csv input file
data = pd.read_csv(Input)
#cleaning data to drop any possible empty values
data.dropna(inplace=True)

#sorting data by column values
data_sorted = data.groupby(["Border","Date","Measure"],as_index=False)

#create new dataframe sorted by index  
data_new = data_sorted.agg({"Value":'sum'}).sort_index()

#adding on new "Average" column to data frame sorted by index
data_new['Average'] = round(data_new['Value'].rolling(window=5, center=False).mean())

#sorting final output by column values
data_final = data_new.sort_values(["Date","Border","Measure"],ascending=[False,False,False])

#print dataframe to output file without index on dataframe
pd.DataFrame(data_final).to_csv(Output_path,index=False)

   




