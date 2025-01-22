from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///:memory:')
metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

metadata.create_all(engine)
connection = engine.connect()
connection.execute(users.insert(), [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}])
result = connection.execute(users.select()).fetchall()
print(result)
