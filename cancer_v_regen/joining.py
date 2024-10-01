import pandas as pd

# load the data
df1 = pd.read_excel("/Users/vishnu/Downloads/1dpl_v_contrast.xlsx")
df2 = pd.read_excel("/Users/vishnu/Downloads/4dpl_v_contrast.xlsx")
df3 = pd.read_excel("/Users/vishnu/Downloads/7dpl_v_contrast.xlsx")

# rename log2FoldChange column for each dataframe to avoid confusion
df1 = df1.rename(columns={"log2FoldChange": "log2FC_day1"})
df2 = df2.rename(columns={"log2FoldChange": "log2FC_day4"})
df3 = df3.rename(columns={"log2FoldChange": "log2FC_day7"})

# merge the data
merged_df = pd.merge(df1, df2, on='gene name', how='outer')
merged_df = pd.merge(merged_df, df3, on='gene name', how='outer')

# write the data to a new Excel file
merged_df.to_excel("regen_combined.xlsx", index=False)
