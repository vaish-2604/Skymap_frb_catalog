# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:50:25 2024

@author: vaishu
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
import pandas as pd
file='Users\vaishu\Desktop\project shit\Skymap\frb_catalog.csv'
df= pd.read_csv("frb_catalog.csv")
ra=df['ra'].values
dec=df['dec'].values
# Dummy data for demonstration purposes
# Replace this with the actual data from the FBR catalog

# Convert RA and Dec to SkyCoord object
coords = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')

# Plotting the sky map
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(coords.ra.wrap_at(180*u.degree).radian, coords.dec.radian, s=5, color='blue', alpha=0.5)
ax.set_xlim(np.pi, -np.pi)
ax.set_ylim(-np.pi/2, np.pi/2)
ax.set_xlabel('RA (radian)')
ax.set_ylabel('Dec (radian)')
ax.set_title('FBR Catalog Sky Map')
ax.grid(True)
plt.show()
