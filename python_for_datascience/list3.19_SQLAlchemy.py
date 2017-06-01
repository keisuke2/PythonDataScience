import sqlalchemy
print("リスト3.19:SQLAlchemyでDB接続")
#create_engineにはDBのURLを渡す
engine = sqlalchemy.create_engine("sqlite:///iris.db")
print("リスト3.20:SQLAlchemyでデータを読み出す")
sql = "SELECT * FROM iris WHERE Species = ?"
species = "virginica"
cursor = engine.execute(sql, (species, ))
for row in cursor:
	print("Sepal Length:", row[0], "Sepal Width:",row[1], "Petal Length:", row[2], "Petal Width:", row[3], "Species:",row[4])
