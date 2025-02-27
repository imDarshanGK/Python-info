from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Create an in-memory SQLite database engine
engine = create_engine('sqlite:///:memory:')
metadata = MetaData()

# Define the 'users' table with an additional 'email' column
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer),
    Column('email', String)  # New column
)

# Create the table in the database
metadata.create_all(engine)

# Establish a connection to the database
connection = engine.connect()

# Insert new data into the 'users' table, including the email field
connection.execute(users.insert(), [
    {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},
    {'name': 'Bob', 'age': 30, 'email': 'bob@example.com'},
    {'name': 'Charlie', 'age': 35, 'email': 'charlie@example.com'},
    {'name': 'David', 'age': 22, 'email': 'david@example.com'}
])

# Query users who are older than 25
result = connection.execute(users.select().where(users.c.age > 25)).fetchall()

# Print the result of the query
print(result)

# Close the connection gracefully
connection.close()
