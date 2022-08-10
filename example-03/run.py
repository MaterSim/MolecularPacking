from pyxtal.db import database
from pyxtal.msg import AtomTypeError, ReadSeedError
import numpy as np
import pandas as pd

db = database('../dataset/shape.db')

for i, p in enumerate([(0, 19), (19, -1)]):
    (i1, i2) = p
    name = 'shape-'+str(i)
    sphs = []
    codes = []
    for i, code in enumerate(db.codes[i1:i2]):
        try:
            row = db.get_row(code)
            xtal = db.get_pyxtal(code)
            if row.mol_smi.find('F') > -1: xtal.substitute({'F': 'Cl'})
            sph = xtal.get_spherical_images()
            sphs.append(sph)
            print(i, code)
        except ReadSeedError as e:
            print('SeedError', i, code) #, e.message)
        except AtomTypeError as e:
            print('AtomTypeError', i, code, e.message)
    
    d={'Code': codes}
    df = pd.DataFrame(d)
    df.to_csv(name+'.csv', index=False)

    vals = np.eye(len(codes))
    for i in range(len(sphs)-1):
        sph1 = sphs[i]
        for j in range(i+1, len(sphs)):
            sph2 = sphs[j]
            S = sph1.get_similarity(sph2, M=10, cutoff=0.95).mean()
            vals[i, j] = S
            vals[j, i] = S
    np.savetxt(name+'.txt', vals)
