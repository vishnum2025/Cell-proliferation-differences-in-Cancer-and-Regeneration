# BiocManager::install("rtracklayer")

library(rtracklayer)

gtf_file <- "/Users/vishnu/Danio_rerio.GRCz11.109.gtf"
gtf_granges <- import(gtf_file, format = "gtf")
gtf_df <- as.data.frame(gtf_granges)
#install.packages("openxlsx")  
#library(openxlsx)
write.xlsx(gtf_df, "/Users/vishnu/gtf_df.xlsx")
unique(gtf_df$gene_biotype)
filtered_df <- gtf_df[gtf_df$gene_biotype != "protein_coding", ]
#write.csv(degs_df, "filtered_df.csv")

ncbi <- "/Users/vishnu/NCBI lnc list.csv"
ncbi_df <- read.csv(ncbi)
ncbi_genes <- ncbi_df$gene_name

filtered_granges <- gtf_granges[gtf_granges$gene_name %in% ncbi_genes]

num2_df <- data.frame(
  gene_name = mcols(filtered_granges)$gene_name,
  gene_type = mcols(filtered_granges)$gene_biotype
)
num2_df <- num2_df[!duplicated(num2_df), ]
num2_df <- num2_df[num2_df$gene_type != "protein_coding", ]


degs <- "/Users/vishnu/degs_latest.csv"
degs_df <- read.csv(degs)
deg_genes <- degs_df$X

gtf_subset <- filtered_df[c("gene_name", "gene_biotype")]
genes_present_df2 <- merge(gtf_subset, degs_df, by.x = "gene_name", by.y = 1)
genes_present_df2<- genes_present_df2[!duplicated(genes_present_df2$gene_name), ]

output_file <- "genes_present_df2.csv"
write.csv(genes_present_df2, file = output_file, row.names = FALSE)




