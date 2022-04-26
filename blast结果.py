import json
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


file_ = open("result_core_genes_2027_pangenomes.json")
file = json.load(file_)
file_.close()

result_dict = dict()
result_dict_n = dict()
for entry in file["BlastOutput2"]:
    query = entry["report"]["results"]["search"]
    name_query = query["query_title"]
    len_query = query["query_len"]
    n = len(query["hits"])
    result_dict[name_query] = n
    if n > 1:
        result_dict_n[name_query] = []
        hits = query["hits"]
        for hit in hits:
            for hsp in hit["hsps"]:
                hsp_result = dict()
                hsp_result["contig"] = hit["description"][0]["id"]
                hsp_result["hit_from"] = hsp["hit_from"]
                hsp_result["hit_to"] = hsp["hit_to"]
                hsp_result["seq"] = hsp["hseq"]
                mismatch = hsp['align_len'] - hsp['identity']
                hd = mismatch
                if len_query > hsp['align_len']:
                    hd = len_query - hsp['align_len'] + mismatch
                query_coverage = 1 - hd / len_query
                hsp_result["coverage"] = query_coverage
                result_dict_n[name_query].append(query_coverage)
print(result_dict_n)
# 找到有2个0.9 coverage以上的结果
double_gene = []
for k,v in result_dict_n.items():
    for p in v[1:]:
        if p > 0.9:
            double_gene.append(k)
print("double",double_gene)
#
result_double = dict()
for entry in file["BlastOutput2"]:
    query = entry["report"]["results"]["search"]
    name_query = query["query_title"]
    len_query = query["query_len"]
    n = len(query["hits"])
    if name_query in double_gene:
        result_double[name_query] = []
        hits = query["hits"]
        for hit in hits:
            for hsp in hit["hsps"]:
                name = hit["description"][0]["id"]
                result_double[name_query].append(name)
gene_list = []

for k,v in result_double.items():
    for gene in v:
        gene_list.append(gene)

print(gene_list)


# # 去除有2个以上结果的基因
# my_record = []
#
# records = SeqIO.parse("Sc_core_genes_complete.fa","fasta")
# for record in records:
#     if record.id not in gene_list:
#         gene = SeqRecord(record.seq, record.id,  description="")
#         my_record.append(gene)
# print(len(my_record))
# SeqIO.write(my_record, "Sc_core_genes_2034.fa", "fasta")
