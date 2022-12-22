# File che utilizzeremo in futuro :D
from dao.productLinesDao import ProductLines

result=ProductLines.getAllProductLines()
for r in result:
    print(r)