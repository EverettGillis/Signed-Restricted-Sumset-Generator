# Signed-Restricted-Sumset-Generator

**About**
\
\
Generate and examine h-fold signed, restricted sumsets. 

\
**Overview**
\
\
Let $A$ be of size $m$ and a subset of an abelian group $G$ of order $n$. We are interested in the $h$-fold signed restricted sumset of $A$ defined as
$$h\hat{\_{\pm}}A=\lbrace \lambda\_{1}a_{1}+\cdots+\lambda\_{m}a\_{m} \\ \: \\ \lambda\_{1},\ldots,\lambda\_{m}\in\lbrace-1,0,1\rbrace,\\ |\lambda\_{1}|+\cdots+|\lambda\_{m}|=h \rbrace.$$
Using the sumset generator, we may easily characterize the smallest $h$-fold signed restricted sumset of $A$, defined as
$$\rho\hat{\_{\pm}}(n, m, h)=\min\lbrace |h\hat{\_{\pm}}A|\mid A \subseteq G,|A|=m\rbrace ,$$
for desired $n$, $m$, and $h$.

\
**Intended Use**
\
\
```Signed Restricted Sumset Generator.py``` iterates over desired values of $n$, $m$, and $h$ to calculate minimum sumset size.<br/>
Requirements: Python 3.10.

```Data Analysis Tool.py``` analyzes data retrieved from a local .xlsx file. Allows for pattern tests, selection of subcases, and 3D graphical representations. Current version requires that paths of .xlsx files and/or subsheets be specified, and that custom analysis be hard-coded.<br/>
Requirements: Python 3.10, pandas 1.4.2, NumPy 1.22.3, matplotlib 3.5.2.

\
**Citations**
\
\
Gillis, E. (2022) On the Minimum Size of an h-fold Signed Restricted Sumset. Research Papers in Mathematics, B. Bajnok, ed., Gettysburg College, Vol. 25.
