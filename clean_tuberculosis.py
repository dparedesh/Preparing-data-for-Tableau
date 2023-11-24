""" Clean tuberculosis data

This script is intended to clean the tuberculosis dataset, dedicated
mainly to rename the columns of the original dataset DATA_FILE using the
dictionary provided VAR_FILE
"""

import pandas as pd

DATA_FILE = "data/Tuberculosis/TB_burden_countries_2023-11-22.csv"

VAR_FILE = "data/Tuberculosis/TB_data_dictionary_2023-11-22.csv"

CLEANED_FILE = "data/Tuberculosis/tuberculosis.csv"


def main():

    """
    Rename variables of DATA_FILE using the names from VAR_FILE
    File with renamed variables is written in CLEANED_FILE.
    """

    data = pd.read_csv(DATA_FILE)

    var = pd.read_csv(VAR_FILE)

    data_names = list(data.columns)

    var_names = {'year': 'year'}

    for col in data_names:

        if col == 'year':
            continue
        var_name = var[var['variable_name'] == col]['definition']
        var_names[col] = var_name.iat[0]

    data.rename(columns=var_names, inplace=True)

    data.to_csv(CLEANED_FILE)


if __name__ == "__main__":
    main()
