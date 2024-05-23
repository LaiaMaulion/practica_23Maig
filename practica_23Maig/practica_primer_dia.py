from pathlib import Path
import os
import sisl 
import sisl.viz
import numpy as np

from ase.build import molecule
atoms = molecule('C6H6', vacuum=5)
benze=sisl.Geometry.new(atoms)
resul=Path('resul')
benze.write(resul/'geom.fdf')

with open(resul/'RUN.fdf', 'w') as f:
    f.write('%include geom.fdf\n')
    f.write('TS.TH.Save true')

