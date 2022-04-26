import json
import os
import pandas as pd

gene_list = []
for a in os.listdir(r"D:\python\cgMLST_SC\4.core_genes\5. Ridom验证\core_genes_1492"):
    gene_list.append(a.split(".")[0])


file = open(r"D:\python\cgMLST_SC\4.core_genes\5. Ridom验证\核心基因分布\core_genes_CR01.json")
f = json.load(file)
file.close()
# 在每个query中进行
query_list = []


result = {"name":[], "type":[], "start":[], "end":[], "strand":[]}
querys = f["BlastOutput2"]
for query in querys:
    results = query["report"]["results"]["search"]
    # query_name = results["query_id"]
    query_name = results["query_title"]
    query_len = results["query_len"]
    hits = results["hits"]
    for hit in hits:
        hsp = hit["hsps"][0]
        result["name"].append(query_name)
        result["start"].append(min(hsp["hit_from"], hsp["hit_to"]))
        result["end"].append(max(hsp["hit_from"], hsp["hit_to"]))
        if hsp["hit_strand"] == "Plus":
            result["strand"].append("+")
        else:
            result["strand"].append("-")
        result["type"].append("CDS")
        query_list.append(query_name)

df = pd.DataFrame(result)
print(df)
df.to_excel("core_genes.xlsx")
# print(len(query_list))
# print(len(gene_list))
# for a in gene_list:
#     if a not in query_list:
#         print(a)
