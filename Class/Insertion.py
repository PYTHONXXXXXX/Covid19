

from Class.Sqlite import Sqlite

class Insertion(Sqlite):
    def __init__(self,db_name,table_name,values):
        super().__init__(db_name,table_name)
        self.table_name=table_name
        self.values=values
    def insert(self):
        
        sql_description='insert into {} ({}) values({})'.format(self.table_name,self.colum_pk+","+','.join(self.colum_name),','.join(self.colum_count))
        return sql_description
        
    def execute(self):
       
        self.cursor.executemany(self.insert(),self.values)
        self.db.commit()
        
        




