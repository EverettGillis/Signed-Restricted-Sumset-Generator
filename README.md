# Signed-Restricted-Sumset-Generator

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
'''Signed Restricted Sumset Generator.py''' iterates over desired values of $n$, $m$, and $h$ to calculate minimum sumset size.
Requirements: Python 3.10.

'''Data Analysis Tool.py''' retreives analyzes local data in .xlsx file. Allows for selection of subcases, pattern tests, and graphical representation. Current version requires that paths of .xlsx files and/or subsheets be specified, and custom analysis be hard-coded.
Requirements: Python 3.10, pandas, numpy, matplotlib.

\
**Citations**
\
\
E. Gillis, On the Minimum Size of an h-fold Signed Restricted Sumset. Research Papers in Mathematics, B. Bajnok, ed., Gettysburg College, Vol. 25 (2022).
