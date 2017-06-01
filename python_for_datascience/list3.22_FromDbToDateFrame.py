import sqlalchemy
import pandas as pd
print("リスト3.22:DBからDateFrameへの取り込み")
db_url = "sqlite:///iris.db"
sql = "SELECT * FROM iris"
engine = sqlalchemy.create_engine(db_url)
iris_data = pd.read_sql(sql, engine)
print("条件なし")
print(iris_data)
print("加工済みデータをDateFrameに")
sql = """SELECT * FROM iris WHERE Species = '{0}' AND "Petal Width" >= {1}""".format("versicolor", 1.5)
versicolor = pd.read_sql(sql, engine)
versicolor
print("条件指定:種(Species)　versicolor, 花弁の長さ(Petal Width)1.5以上")
print(versicolor)