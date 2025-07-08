import psycopg2


class Database:
    def __init__(
        self,
        host: str,
        db_name: str,
        username: str,
        password: str,
    ):
        self.host = host
        self.db_name = db_name
        self.username = username
        self.password = password

    def get_connection_string(self) -> str:
        return (
            f"postgresql://{self.username}:{self.password}@{self.host}/{self.db_name}"
        )

    def get_connection(self) -> psycopg2.extensions.connection:
        return psycopg2.connect(self.get_connection_string())
