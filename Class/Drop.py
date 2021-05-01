from Class.Sqlite import Sqlite


class Drop(Sqlite):
    def __init__(self,db_name,table_name):
        super().__init__(db_name,table_name)
        self.table_name=table_name

    def drop(self):
        sql_description="DROP TABLE {}".format(self.table_name)
        return sql_description
    def execute(self):
        self.cursor.execute(self.drop())
        