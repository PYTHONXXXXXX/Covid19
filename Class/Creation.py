from Class.Sqlite import Sqlite

class Creation(Sqlite):
    def __init__(self,db_name,table_name,**colums):
        super().__init__(db_name,table_name)
        self.table_name=table_name
        self.colums=colums
    def create(self):
        li1=[]
        for data in self.colums.items():
            if data[1]['pk']:data[1]['pk']='PRIMARY KEY' 
            else: data[1]['pk']=''
            if not data[1]['null']:data[1]['null']='NOT NULL'
            else:data[1]['null']=''
            li1.append(data[0]+" "+data[1]['type']+" "+data[1]['pk']+" "+data[1]['null'])
           
            sql_description='''CREATE TABLE {}({});'''.format(self.table_name,','.join(li1))
        return sql_description
    def execute(self):
        self.cursor.execute(self.create())
        

