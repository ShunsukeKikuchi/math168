import numpy as np
import scanpy as sc
import loompy as lp
from typing import Optional, Union, List

def convert_h5ad_to_loom(
    h5ad_file: str,
    output_loom: Optional[str] = None,
) -> str:

    print(f"Loading h5ad file: {h5ad_file}")
    adata = sc.read_h5ad(h5ad_file)
    adata.obs['Cell.Type'] = adata.obs['Cell.Types'].str.replace('.', '_')

    row_attrs = { 
        "Gene": np.array(adata.var["feature_name"]) ,
        }

    col_attrs = { 
        "CellID":  np.array(adata.obs.index) ,
        "nGene": np.array( np.sum(adata.X.transpose()>0 , axis=0)).flatten() ,
        "nUMI": np.array( np.sum(adata.X.transpose() , axis=0)).flatten() ,
        "Cell.Type": np.array(adata.obs['Cell.Types']),
    }

    lp.create(output_loom, adata.X.transpose(), row_attrs, col_attrs)
    print(f"Loom file created: {output_loom}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert h5ad file to loom format for pySCENIC')
    parser.add_argument('h5ad_file', type=str, help='Path to input h5ad file')
    parser.add_argument('--output', '-o', type=str, default=None, help='Path to output loom file')
    
    args = parser.parse_args()
    
    convert_h5ad_to_loom(
        args.h5ad_file,
        args.output,
    )

    # python create_loom.py ../alz.h5ad -o ../alz.loom
