from pyxtal.db import database
import pandas as pd
import numpy as np

db = database('../dataset/hydrocarbon.db')

codes = ['BEANTR',
         'PHENAN',
         'NAPHTA',
         'BIPHEN',
         'ANTCEN',
         'QUPHEN',
         'CRYSEN',
         'ZZZOYC01',
         'BZPHAN',
         'TRIPHE',
         'NAPPYR03',
         'BNPYRE10',
         'TBZPYR',
         'BOXGAW01',
         'CORONE',
         'HBZCOR',
         'CORXAI10',
         'OVALEN',
         'KEKULN10',
         'DBPERY',
         'DBZCOR',
         'BENZEN',
         'DBNTHR01',
         'BNPERY',
         'DNAPAN',
         'PERLEN01',
         'QUATER10',
         'TBZPER',
         'PYRENE',
         'NAPANT01'
        ]

# Save the list
d={'Code': codes}
df = pd.DataFrame(d)
df.to_csv('PAH.csv', index=False)

sphs = []
for i, code in enumerate(codes):
    print(i, code)
    xtal = db.get_pyxtal(code)
    sph = xtal.get_spherical_images()
    sphs.append(sph)

vals = np.eye(len(codes))
for i in range(len(sphs)-1):
    sph1 = sphs[i]
    for j in range(i+1, len(sphs)):
        sph2 = sphs[j]
        S = sph1.get_similarity(sph2, M=8, cutoff=0.95).mean()
        vals[i, j] = S
        vals[j, i] = S
        print(i, j, S)
# Save the distances
np.savetxt('PAH.txt', vals)

