## download data
```bash
wget https://datasets.cellxgene.cziscience.com/5d871206-9489-4d9f-8106-94305ccb1c3a.h5ad
mv 5d871206-9489-4d9f-8106-94305ccb1c3a.h5ad alz.h5ad
```

## SCENIC

```bash
cd SCENIC
```

- Create loom file from h5ad:
   ```bash
   python pySCENIC/loom.py alz.h5ad alz.loom
   ```

- Run SCENIC inference:
   ```bash
   bash pyscenic.sh
   ```

## SCING

```bash
cd SCING/Python_Codes
```

- Create supercells:
   ```bash
   bash supercells.sh
   ```

- Build gene regulatory network:
   ```bash
   bash buildnet.sh
   ```

- Merge results:
   ```bash
   bash merge.sh
   ```

## CellOracle
 ```bash
 cd CellOracle
 ```
- Submit analysis job:
   ```bash
   bash submit.sh
   ```
