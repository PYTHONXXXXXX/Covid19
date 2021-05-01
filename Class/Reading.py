from Class.Sqlite import Sqlite


class Reading(Sqlite):
    def __init__(self,db_name,table_name,Country=None,row_or_colum=True):
        super().__init__(db_name,table_name)
        self.table_name=table_name
        self.country=Country
        self.read_datas=None
        self.row_or_colum=row_or_colum
    def read(self):
        if self.row_or_colum:
            if self.country != None:
                sql_description='select * from {} where {}="{}"'.format(self.table_name,self.colum_pk,self.country)
                return sql_description
            
            sql_description='select * from {}'.format(self.table_name)
            return sql_description

    def execute(self):
        self.read_datas=self.cursor.execute(self.read()).fetchall()
        
