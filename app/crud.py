import pandas as pd


class CRUD:
    def __init__(self, db):
        self.conn = db.get_connection()

    def get_all_temperatures(self):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "SELECT timestamp, temperature, humidity, name AS room FROM records INNER JOIN devices ON records.device_id = devices.id LIMIT 4"
            )
            return cursor.fetchall()

    def get_temp_df(self) -> pd.DataFrame:
        df = pd.read_sql_query(
            "SELECT timestamp, name, temperature, humidity FROM records INNER JOIN devices ON devices.id = records.device_id LIMIT 4",
            self.conn,
        )
        return df
