import psycopg2


class DatabaseConnection:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'postgres'
        self.password = '20092002'
        self.database = 'face_id'
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(host=self.host, user=self.user, password=self.password,
                                           database=self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
