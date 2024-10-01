
BiocManager::install("org.Dr.eg.db")
BiocManager::install("GSEABase")
BiocManager::install("fgsea")
library(GSEABase)
library(fgsea)

res_df <- norm_all

original_gene_list1 <- res_df$stat

names(original_gene_list1) <- res_df$ensembl_id

original_gene_list1<-na.omit(original_gene_list1)

original_gene_list1 = sort(original_gene_list1, decreasing = TRUE)


library(org.Dr.eg.db)

organism <- "org.Dr.eg.db"

BiocManager::install(organism, character.only = TRUE)
library(organism, character.only = TRUE)


BiocManager::install("clusterProfiler", version = "3.16")
BiocManager::install("pathview")
BiocManager::install("enrichplot")
BiocManager::install("GO.db", version = "3.16")
BiocManager::install("HDO.db", version = "3.16")
library(clusterProfiler)
library(enrichplot)
# we use ggplot2 to add x axis labels (ex: ridgeplot)
library(ggplot2)



gse <- gseGO(geneList=original_gene_list1, 
             ont ="BP", 
             keyType = "ENSEMBL", 
             nPerm = 10000, 
             minGSSize = 3, 
             maxGSSize = 800, 
             pvalueCutoff = 0.05, 
             verbose = TRUE, 
             OrgDb = organism, 
             pAdjustMethod = "none")

gseaplot(gse, geneSetID = 1)
require(DOSE)
dotplot(gse, showCategory=10, split=".sign") + facet_grid(.~.sign)

pathway_names <- gse$Description
enrichment_scores <- gse$enrichmentScore

sorted_scores <- sort(enrichment_scores, decreasing = TRUE)
ids<-bitr(names(original_gene_list1), fromType = "ENSEMBL", toType = "ENTREZID", OrgDb=organism)
dedup_ids = ids[!duplicated(ids[c("ENSEMBL")]),]
df2 = res_df[res_df$ensembl_id %in% dedup_ids$ENSEMBL,]
df2$Y = dedup_ids$ENTREZID

kegg_gene_list <- df2$rank
names(kegg_gene_list) <- df2$Y

kegg_gene_list<-na.omit(kegg_gene_list)

kegg_gene_list = sort(kegg_gene_list, decreasing = TRUE)

kegg_organism = "dre"
kk2 <- gseKEGG(geneList     = kegg_gene_list,
               organism     = kegg_organism,
               nPerm        = 10000,
               minGSSize    = 3,
               maxGSSize    = 800,
               pvalueCutoff = 0.05,
               pAdjustMethod = "none",
               keyType       = "ncbi-geneid")
dotplot(kk2, showCategory = 10, title = "Enriched Pathways" , split=".sign") + facet_grid(.~.sign)

kegg_dfzb <- as.data.frame(kk2)

colnames(kegg_dfzb)
write.csv(kegg_dfzb, "kegg_resultszb2.csv", row.names = FALSE)
write.csv(df2, "kegg_geneszb.csv", row.names = TRUE)


