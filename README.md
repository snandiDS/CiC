# cic

This package is to create some special cases of Euler diagram. This package creates representations of set-subset-subsubset (intersections between the set and its subsets).

# Limitation:
This package should not be used to create venn diagrams, as it will not represent the overlaps/intersections between two sets.

The package is built on Arch: x86\_64 bit system; OS: RedHat based (Fedora release 36); and Language: Python (3.9.7) and C.


# Implementation:

In Python:
```
from libmod import cicfn as cic
data = [4090,1062,961]
cic.drawCircles({'data': data, 'color' : ["blue","red","green"], "title": "someting"})
```
