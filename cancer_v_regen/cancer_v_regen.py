import pandas as pd


df_cancer = pd.read_excel('/Users/vishnu/Downloads/zf_brain_cancer_all.xlsx')
df_regeneration = pd.read_excel('/Users/vishnu/Downloads/regen_combined.xlsx')


cancer_genes = set(df_cancer['gene_name'])
regeneration_genes = set(df_regeneration['gene name'])



#  exclusive cancer genes
exclusive_cancer_genes = cancer_genes - regeneration_genes
df_exclusive_cancer_genes = df_cancer[df_cancer['gene_name'].isin(exclusive_cancer_genes)]
df_exclusive_cancer_genes.to_excel('exclusive_cancer_genes.xlsx', index=False)

# exclusive regeneration genes
exclusive_regeneration_genes = regeneration_genes - cancer_genes
df_exclusive_regeneration_genes = df_regeneration[df_regeneration['gene name'].isin(exclusive_regeneration_genes)]
df_exclusive_regeneration_genes.to_excel('exclusive_regeneration_genes.xlsx', index=False)


# common genes

df_regeneration.rename(columns={"gene name": "gene_name"}, inplace=True)
df_cancer = df_cancer.rename(columns={"log2FoldChange": "log2FC_cancer"})
df_common_genes = pd.merge(df_cancer, df_regeneration, on='gene_name', how='inner')
df_common_genes.to_excel('common_genes_combined.xlsx', index=False)















##cancer genes & source
# df_final_output = pd.read_excel('/Users/vishnu/Downloads/final_output.xlsx')

# final_output_genes = set(df_final_output['name'])

# common_genes = cancer_genes & final_output_genes
# df_common_genes = df_final_output[df_final_output['name'].isin(common_genes)]
# df_common_genes = df_common_genes[['name', 'source_csv', 'log2FoldChange']]
# df_common_genes.to_excel('cancer_genes_with_source.xlsx', index=False)
