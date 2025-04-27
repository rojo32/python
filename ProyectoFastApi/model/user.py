from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

# el nombre de la tabla es 'user', se pasa la metadata, se indica el nombre de las columna con su tipo de dato
user= Table("users",meta_data, Column("id", Integer, primary_key=True),
                            Column("name",String(250), nullable=False),
                            Column("username",String(255),nullable=False),
                            Column("password",String(255),nullable=False))

meta_data.create_all(engine)