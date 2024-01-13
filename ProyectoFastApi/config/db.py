"""conexion a la BD"""
from sqlalchemy import create_engine,MetaData

#indicamos que vamos a trabajar con musql y pymysql, luego pasamos el usuario y clave, servidor,puerto y base de datos
engine= create_engine("mysql+pymysql://root:argelioramos@localhost:3306/base_datos")

conn= engine.connect()
meta_data=MetaData()

