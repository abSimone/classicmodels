# File che utilizzeremo in futuro :D

from dao.gruppo3Dao import Gruppo3Dao
result = Gruppo3Dao.getEmployeeAndOrdersInfoByCustomer()
for res in result:
    print(f"\n{res}")