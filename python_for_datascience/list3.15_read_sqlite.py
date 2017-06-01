import sqlite3

print("SQLiteをopen")
con = sqlite3.connect("iris.db")
print("SQLiteからデータを読み出す")
sql = "SELECT * FROM iris WHERE Species = ?"
species = "virginica"
cursor = con.execute(sql, (species, ))
for row in cursor:
	print("Sepal Length:", row[0], "Sepal Width:",row[1], "Petal Length:", row[2], "Petal Width:", row[3], "Species:",row[4])