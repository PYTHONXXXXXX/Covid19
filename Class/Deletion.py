from Class.Sqlite import Sqlite
class Deletion(Sqlite):
    def __init__(self,db_name,table_name,delete_data):
        super().__init__(db_name,table_name)
        self.table_name=table_name
        self.delete_data=delete_data
    def delete(self):
        pass
    def execute(self):
        pass