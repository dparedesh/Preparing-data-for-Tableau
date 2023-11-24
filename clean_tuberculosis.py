import pandas as pd


data_file = "data/Tuberculosis/TB_burden_countries_2023-11-22.csv"

var_file = "data/Tuberculosis/TB_data_dictionary_2023-11-22.csv"


data = pd.read_csv(data_file)

var = pd.read_csv(var_file)

data_cols = list(data_df.columns)

var_names = {'year':'year'}

for col in data_cols:

	if col == 'year': continue
	var_name = var_names[var_names['variable_name'] == col]['definition']
	var_names[col] = var_name.iat[0]


data.rename(columns = var_names,inplace=True)

data.to_csv("data/tuberculosis/tuberculosis_2022.csv")


