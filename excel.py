import pandas as pd

df = pd.read_excel("Staphylococcus capitis cgMLST test4 cgMLST v8.xlsx")

col = df.columns.to_list()[2:-1]
count_result = dict()
for gene in col:
    gene_count = df[gene].value_counts()
    count_result[gene] = []
    if "? (not found)" in gene_count.index:
        num_not_found = df[gene].value_counts().loc["? (not found)"]

    else:
        num_not_found = 0
    count_result[gene].append(num_not_found)
    if "? (failed)" in gene_count.index:
        num_failed = df[gene].value_counts().loc["? (failed)"]

    else:
        num_failed = 0
    count_result[gene].append(num_failed)
    num_gene_good = 386 - num_failed - num_not_found
    count_result[gene].append(num_gene_good)
    count_result[gene].append(num_gene_good/386) # ["good_percent"] =


df_res = pd.DataFrame(count_result)
print(df_res)
df_res.to_excel("Sc_core_genes_ridom_统计V8_ncbi+nature.xlsx")

# ? (not found)
# ? (failed)