import celloracle as co

# 0. Import

import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import seaborn as sns

# %%

h5ad_path = "/u/home/s/skikuchi/project-xyang123/math168/alz.h5ad"

os.chdir("/u/home/s/skikuchi/project-xyang123/math168/CellOracle")

# %%
adata = sc.read_h5ad(h5ad_path)
print(f"Cell number is :{adata.shape[0]}")
print(f"Gene number is :{adata.shape[1]}")

# %%
# Load TF info which was made from mouse cell atlas dataset.
base_GRN = co.data.load_human_promoter_base_GRN() # human
# Check data

base_GRN["gene_short_name"] = base_GRN["gene_short_name"].str.upper()

base_GRN.head()
base_GRN.columns = base_GRN.columns.str.upper()

# %%
# Instantiate Oracle object
oracle = co.Oracle()

# %%
# Check data in anndata
print("Metadata columns :", list(adata.obs.columns))
print("Dimensional reduction: ", list(adata.obsm.keys()))

# %%
adata.var.index = adata.var.index.str.upper()

# %% [markdown]
# CHeck if this is raw count. If not, see documentation

# %% [markdown]
# ###Need to make embedding X_draw_graph_fa -> sc.tl.draw_graph

# %%
adata.obsm

# %%
sc.pp.pca(adata, n_comps=50)

sc.pp.neighbors(adata, use_rep="X_pca", n_neighbors=30)

# %%
sc.tl.draw_graph(adata, layout="fa")

# %%
adata.obs["louvain"] = '0'

# %%
adata

# %%
# Instantiate Oracle object.
oracle.import_anndata_as_raw_count(adata=adata,
                                   cluster_column_name="louvain",
                                   embedding_name="X_draw_graph_fa")

# %%
# replace columns name
# Replace column names using a dictionary
column_mapping = {"PEAK_ID": "peak_id", "GENE_SHORT_NAME": "gene_short_name"}
base_GRN = base_GRN.rename(columns=column_mapping)

# %%
# You can load TF info dataframe with the following code.
oracle.import_TF_data(TF_info_matrix=base_GRN)

Paul_15_data = pd.read_csv("temp/TF_data_in_Paul15.csv")
Paul_15_data["TF"] = Paul_15_data["TF"].str.upper()
Paul_15_data["Target_genes"] = Paul_15_data["Target_genes"].str.upper()

# %%
# Make dictionary: dictionary key is TF and dictionary value is list of target genes.
TF_to_TG_dictionary = {}

for TF, TGs in zip(Paul_15_data.TF, Paul_15_data.Target_genes):
    # convert target gene to list
    TG_list = TGs.replace(" ", "").split(",")
    # store target gene list in a dictionary
    TF_to_TG_dictionary[TF] = TG_list

# We invert the dictionary above using a utility function in celloracle.
TG_to_TF_dictionary = co.utility.inverse_dictionary(TF_to_TG_dictionary)

# %%
# Add TF information 
oracle.addTFinfo_dictionary(TG_to_TF_dictionary)

# %%
# Perform PCA
oracle.perform_PCA()

# Select important PCs
plt.plot(np.cumsum(oracle.pca.explained_variance_ratio_)[:100])
n_comps = np.where(np.diff(np.diff(np.cumsum(oracle.pca.explained_variance_ratio_))>0.002))[0][0]
plt.axvline(n_comps, c="k")
plt.show()
print(n_comps)
n_comps = min(n_comps, 50)

# %%
n_cell = oracle.adata.shape[0]
print(f"cell number is :{n_cell}")


k = int(0.025*n_cell)
print(f"Auto-selected k is :{k}")

oracle.knn_imputation(n_pca_dims=n_comps, k=k, balanced=True, b_sight=k*8,
                      b_maxl=k*4, n_jobs=4)

# %%
# Save oracle object.
oracle.to_hdf5("temp/Paul_15_data.celloracle.oracle")
# Load file.
oracle = co.load_hdf5("temp/Paul_15_data.celloracle.oracle")

# %%
# Check clustering data
sc.pl.draw_graph(oracle.adata, color="louvain")

# %%
adata.var

# %%
# Calculate GRN for each population in "louvain_annot" clustering unit.
# This step may take some time.(~30 minutes)
links = oracle.get_links(cluster_name_for_GRN_unit="louvain", alpha=10,
                         verbose_level=10)

# %%
clusters = links.links_dict.keys()

# %%
for cluster in clusters:
    #Save as csv
    os.makedirs(f"network/", exist_ok=True)
    links.links_dict[cluster].to_csv(f"network/raw_GRN_for_{cluster}.csv")

# %%


# %%


# %%



