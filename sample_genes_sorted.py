import pandas as pd

# Load CSV files
csv1 = pd.read_csv('/Users/vishnu/Downloads/brain development.csv')
csv2 = pd.read_csv('/Users/vishnu/Downloads/cellproliferation_brain.csv')
csv3 = pd.read_csv('/Users/vishnu/Downloads/cell differentiation_brain.csv')

# Load Excel files
xlxs1 = pd.read_excel('/Users/vishnu/Downloads/1dpl_v_contrast.xlsx')
xlxs2 = pd.read_excel('/Users/vishnu/Downloads/4dpl_v_contrast.xlsx')
xlxs3 = pd.read_excel('/Users/vishnu/Downloads/7dpl_v_contrast.xlsx')

# Add source column
csv1['source_csv'] = 'brain_development '
csv2['source_csv'] = 'cell_proliferation'
csv3['source_csv'] = 'cell_diff_brain'

xlxs1['source_xlxs'] = '1dpl'
xlxs2['source_xlxs'] = '4dpl'
xlxs3['source_xlxs'] = '7dpl'

final_df = pd.DataFrame()

# Perform merges for each CSV file and append to final_df
for csv in [csv1, csv2, csv3]:
    for xlxs in [xlxs1, xlxs2, xlxs3]:
        temp_df = pd.merge(csv, xlxs, how='inner', left_on='name', right_on='gene name')
        final_df = pd.concat([final_df, temp_df])

# Remove duplicates
final_df = final_df.drop_duplicates()

# Reshape the dataframe to have one row per gene, with columns for each source_xlxs and log2FoldChange
final_df_pivot = final_df.pivot_table(index=['name', 'source_csv'], 
                                columns='source_xlxs', 
                                values='log2FoldChange',
                                aggfunc='first').reset_index()


# Save output to CSV file
final_df.to_csv('final_output2.csv', index=False)