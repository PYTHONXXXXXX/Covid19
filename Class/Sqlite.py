import sqlite3 as sql

class Sqlite(object):
    def __init__(self,db_name,table_name):
        self.db_name=db_name
        self.table_name=table_name
        self.db=self.connect()
        self.cursor=self.db.cursor()
        
        self.colum_name,self.colum_count,self.colum_pk=self.get_colums_info()
    def get_colums_info(self):
        sql_description='PRAGMA table_info({});'.format(self.table_name)
        colum_info=self.cursor.execute( sql_description).fetchall()
        colum_count_list=[]
        colum_name_list=[]
        colum_pk=""
        for colum in colum_info:
            if colum[5]:colum_pk=colum[1]
            else:colum_name_list.append(colum[1])
            colum_count_list.append('?')
        return colum_name_list, colum_count_list,colum_pk
    def execute(self):
        pass
    def sql_execute(self):
        self.execute()
        self.close()
    def connect(self):
        return sql.connect(self.db_name)
    def close(self):
        self.cursor.close()
        self.db.close()

    
    