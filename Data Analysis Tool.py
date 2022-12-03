# signed restricted sumset data analysis


# df modules
import pandas as pd

# plotting modules
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
  
# Here 0th column will be extracted
df = pd.read_excel(r'C:\INSERT_PATH_HERE\INSERT_EXCEL_FILE_NAME_HERE.xlsx',
                   dtype = {'n': int,
                            'm': int,
                            'h': int,
                            'νˆ±': int,
                            'ρˆ±>=m': str,
                            'prime n': str,
                            'm=h': str,
                            'νˆ±=ρˆ±': str})

selected_data = pd.read_excel(r'C:\INSERT_PATH_HERE\INSERT_EXCEL_FILE_NAME_HERE.xlsx',
                              sheet_name='Selected Data',
                              skiprows=1)#skiprows=1 (default)

# (all data) indexing key
#    n    m    h    νˆ±    ρˆ±    ρˆ±>=m    prime n    m=h    νˆ±=ρˆ±
#    0    1    2    3      4      5         6          7      8

# DATA TOOL: iterate through data to highlight patterns or generate subsets
for i in range(0, 763):
    row = df.iloc[i] # cycle through each row

    # example condition: print only data for which m=h
    if row[1] == row[2]:
        print(str(row[0]) + '\t' + str(row[1]) + '\t' + str(row[2]) + '\t' + str(row[3]) + '\t' + str(row[4]))


# 3D plotting

# (all data) indexing key
#    n    m    h    νˆ±    ρˆ±    ρˆ±>=m    prime n    m=h    νˆ±=ρˆ±
#    0    1    2    3      4      5         6          7      8

# selected_data indexing key
#    n    m    h    νˆ±    ρˆ±
#    0    1    2    3      4


#creating our 3D space using projection=3D parameter
ax = plt.axes(projection='3d')
 
zline = selected_data.iloc[:,4] # vertical (ρˆ±)
xline = selected_data.iloc[:,0] # left (n)
yline = selected_data.iloc[:,1] # right (m=h)

# axis labels
ax.set_xlabel(r'$n$')
ax.set_ylabel(r'$m$')
ax.set_zlabel(r'$\rho\hat{_{\pm}}$')

#using plot3D() method by passing 3 axes values and plotting colour as 'green'
ax.scatter3D(xline, yline, zline, 'green')
plt.show()













