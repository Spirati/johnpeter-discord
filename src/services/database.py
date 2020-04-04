import mysql.connector


class Database:
    def __init__(self, user, password, host, database):
        self.user=user
        self.password=password
        self.host=host
        self.database=database
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database)
        self.cursor = self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()
        self.conn = None
        self.cursor = None

    def add_row(self, headers: list, values: list):
        exec = (f"INSERT INTO {self.database} "
                f"({[header + ',' for header in headers]}) "
                f"VALUES ({[value + ',' for value in values]})")
        with self:
            self.cursor.execute(exec)