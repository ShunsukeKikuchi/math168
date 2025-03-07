
if __name__ == '__main__':
    import os
    import sys
    import warnings
    import scanpy as sc
    sys.path.append('/u/home/s/skikuchi/project-xyang123/SCING/src/')
    from scing import MergeNetworksHelpers as merge
    import glob
    from multiprocessing import Pool, freeze_support
    import pandas as pd
    # Get the path from the command line arguments

    # Set number of threads to use
    nthreads = 12
    os.environ["MKL_NUM_THREADS"] = str(nthreads)
    os.environ["NUMEXPR_NUM_THREADS"] = str(nthreads)
    os.environ["OMP_NUM_THREADS"] = str(nthreads)
    # filter warnings
    warnings.filterwarnings("ignore")

    # data loading
    net_path = '/u/home/s/skikuchi/project-xyang123/math168/SCING/intermediate_networks/'
    out = "/u/home/s/skikuchi/project-xyang123/math168/SCING/"

    save = True

    supercell_path = '/u/home/s/skikuchi/project-xyang123/math168/SCING/supercells.h5ad'
    adata_merged = sc.read_h5ad(supercell_path)

    all_edges = []        
    for path in glob.glob(net_path+'/*.csv.gz'): 
        temp = pd.read_csv(path)
        all_edges.append(temp)
            
    adata_saved = adata_merged.copy()
    #adata_saved.X = adata_saved.X.todense() # same as buildnet we need this
        
    merger = merge.NetworkMerger(adata=adata_saved,
                                networks=all_edges,
                                minimum_edge_appearance_threshold=0.5,
                                prefix='final',
                                outdir="/u/home/s/skikuchi/project-xyang123/math168/SCING/final_network.csv",
                                ncore=12,
                                mem_per_core=int(2e10),
                                verbose=True,
                                cycles=None)#cycles=None?
    merger.preprocess_network_files()
    merger.remove_reversed_edges()
    merger.remove_cycles()
    merger.get_triads()
    merger.remove_redundant_edges()

    merger.save_network()