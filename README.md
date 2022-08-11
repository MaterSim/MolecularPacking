# MolecularPacking
This public repository to compare the crystal packing similarity from the method described in the [arXiv preprint](https://arxiv.org/abs/2207.12548)

It includes the following examples in the format of Jupyter Notebook.

- [example-01-Demo](https://nbviewer.org/github/qzhu2017/MolecularPacking/blob/main/example-01/01-demo.ipynb), a short example to illustrate the idea of spheric image;
- [example-02-PAH](https://nbviewer.org/github/qzhu2017/MolecularPacking/blob/main/example-02/02-PAH.ipynb), clustering the PAH crystals in [Desaraju's 1989 paper](https://doi.org/10.1107/S0108768189003794);
- [example-03-Shape](https://nbviewer.org/github/qzhu2017/MolecularPacking/blob/main/example-03/02-shape.ipynb), clustering the shape examples in [Motherwell's 2010 paper](https://doi.org/10.1039/C0CE00044B).


To run the Jupyter Notebooks on your own environments, you need to install PyXtal via the following command

```
pip install pyxtal>=0.5.2
conda install -c conda-forge rdkit>=2021.09.2
```
