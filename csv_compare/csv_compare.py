import pandas as pd

file1 = "Fields_20231010_errors.csv"
file2 = "diff_obj_file_Fields_20231010.csv"

fields_to_compare = ["ExternalId",  "WIUZ FIELD ID"]

df1 = pd.read_csv(file1, usecols=fields_to_compare)
df2 = pd.read_csv(file2, usecols=fields_to_compare)

diff_df = df1.merge(df2, left_on="ExternalId", right_on="WIUZ FIELD ID", how="outer", indicator=True).loc[lambda x: x['_merge'] == 'left_only']

diff_file = "difference.csv"
diff_df.to_csv(diff_file, index=False)

print(f"Различия сохранены в файл {diff_file}")