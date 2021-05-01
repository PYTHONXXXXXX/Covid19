from Class.Sqlite import Sqlite

class Updation(Sqlite):
    def __init__(self,db_name,table_name,new_values):
        super().__init__(db_name,table_name)
        self.table_name=table_name
        self.new_values=new_values
    def update(self):
        normal_column=[ i+"=?"  for i in self.colum_name]
        sql_description="UPDATE {} SET {}  Where {}=?;".format(self.table_name,",".join(normal_column),self.colum_pk)
        return sql_description
    def format_convert(self):
        new_value_list_=[]
        for new_value in self.new_values:
            new_value_list=list(new_value)
            register=new_value_list[0]
            del new_value_list[0]
            new_value_list.append(register)
            new_value_list_.append(tuple(new_value_list))
        return new_value_list_
    def execute(self):
        self.cursor.executemany(self.update(),self.format_convert())
        self.db.commit()
        
