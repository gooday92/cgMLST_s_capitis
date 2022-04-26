import pandas as pd

path = r"D:\python\2.cgMLST_SC\4.core_genes\5. Ridom验证\导入基因组的检测率\Staphylococcus capitis cgMLST test6.xlsx"
df = pd.read_excel(path)
df["good"] = (1492 - df["#Missing values in Distance Columns"]) / 1492



slide_head = ["Sample ID","#Missing values in Distance Columns", "good"]
df2 = df[slide_head]
print(df2.median())
print(df2.describe())


# path = r"D:\python\cgMLST_SC\4.core_genes\5. Ridom验证\导入基因组的检测率\genes_types.xlsx"
# df = pd.read_excel(path)
#
# res_count = {"gene_name":[], "? (failed)":[], "? (not found)":[], "types":[]}
# for col in df.columns:
#     column = df[col]
#     count = column.value_counts()
#     types_count = len(count.index)
#     res_count["gene_name"].append(col)
#     if "? (failed)" in count.index:
#         res_count["? (failed)"].append(count["? (failed)"])
#         count -= 1
#     else:
#         res_count["? (failed)"].append(0)
#     if "? (not found)" in count.index:
#         res_count["? (not found)"].append(count["? (not found)"])
#         count -= 1
#     else:
#         res_count["? (not found)"].append(0)
#     res_count["types"].append(types_count)
# df = pd.DataFrame(res_count)
# print(df)
# print(df.describe())



