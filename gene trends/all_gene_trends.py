# import pandas as pd

# # Read the three sheets into separate dataframes
# sheet1 = pd.read_excel('/Users/vishnu/Downloads/1dpl_v_contrast.xlsx')
# sheet2 = pd.read_excel('/Users/vishnu/Downloads/4dpl_v_contrast.xlsx')
# sheet3 = pd.read_excel('/Users/vishnu/Downloads/7dpl_v_contrast.xlsx')

# # Merge the gene names from all three sheets into a single set
# all_genes = set(sheet1['gene name']).intersection(set(sheet2['gene name']), set(sheet3['gene name']))

# # Create a new dataframe to store the combined data
# combined_sheet = pd.DataFrame(columns=['gene name', 'log2FoldChange (Day 1)', 'log2FoldChange (Day 4)', 'log2FoldChange (Day 7)'])

# # Iterate through each gene and its log fold change values
# for gene in all_genes:
#     # Check if the gene is present in all three sheets
#     if (gene in sheet1['gene name'].values and
#         gene in sheet2['gene name'].values and
#         gene in sheet3['gene name'].values):
        
#         # Get the log fold change values for the gene in each sheet
#         lfc1 = sheet1.loc[sheet1['gene name'] == gene, 'log2FoldChange'].values[0]
#         lfc2 = sheet2.loc[sheet2['gene name'] == gene, 'log2FoldChange'].values[0]
#         lfc3 = sheet3.loc[sheet3['gene name'] == gene, 'log2FoldChange'].values[0]
        
#         # Append the gene and log fold change values to the combined sheet
#         combined_sheet = pd.concat([combined_sheet, pd.DataFrame([[gene, lfc1, lfc2, lfc3]], columns=combined_sheet.columns)], ignore_index=True)

# # Save the combined sheet to a new Excel file
# combined_sheet.to_excel('combined_data.xlsx', index=False)



import pandas as pd

# Read the combined data sheet
combined_sheet = pd.read_excel('combined_data.xlsx')

# Initialize separate dataframes for each trend
increases_then_decreases_trend = pd.DataFrame(columns=combined_sheet.columns)
increasing_trend = pd.DataFrame(columns=combined_sheet.columns)
decreasing_trend = pd.DataFrame(columns=combined_sheet.columns)

# Iterate through each row in the combined data
for _, row in combined_sheet.iterrows():
    gene_name = row['gene name']
    lfc_day1 = row['log2FoldChange (Day 1)']
    lfc_day4 = row['log2FoldChange (Day 4)']
    lfc_day7 = row['log2FoldChange (Day 7)']
    
    # Check the trend of log2FoldChange values
    if lfc_day1 < lfc_day4 and lfc_day4 > lfc_day7:
        increases_then_decreases_trend = pd.concat([increases_then_decreases_trend, pd.DataFrame([row], columns=combined_sheet.columns)])
    elif lfc_day1 < lfc_day4 < lfc_day7:
        increasing_trend = pd.concat([increasing_trend, pd.DataFrame([row], columns=combined_sheet.columns)])
    elif lfc_day1 > lfc_day4 > lfc_day7:
        decreasing_trend = pd.concat([decreasing_trend, pd.DataFrame([row], columns=combined_sheet.columns)])

# Save the separate sheets to new Excel files
with pd.ExcelWriter('trend_sheets.xlsx') as writer:
    increases_then_decreases_trend.to_excel(writer, sheet_name='increases_then_decreases_trend', index=False)
    increasing_trend.to_excel(writer, sheet_name='increasing_trend', index=False)
    decreasing_trend.to_excel(writer, sheet_name='decreasing_trend', index=False)




print("done")


