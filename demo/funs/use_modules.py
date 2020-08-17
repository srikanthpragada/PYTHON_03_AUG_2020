import sys

sys.path.insert(0, r"c:\classroom\aug3\demo\mylib")
print(sys.path)

import number_funs as nf
from number_funs import ispositive

print(nf.iseven(10))
print(ispositive(-10))
