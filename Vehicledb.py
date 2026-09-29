import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:

    def _init_(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="vehicledb"
        )
        self.cursor = self.conn.cursor()

    def list(self):
        query = "SELECT * FROM Vehicle"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        for row in records:
            print(row)

    def create(self, brand, model, type, price, year):
        query = "INSERT INTO Vehicledb
                   (brand, model, type, price, year)
                   VALUES (%s, %s, %s, %s, %s)"

        data = (brand, model, type, price, year)

        self.cursor.execute(query, data)
        self.conn.commit()

        print("Record created successfully")

    def retrieve(self, id):
        query = "SELECT * FROM Vehicle WHERE id=%s"
        data = (id,)

        self.cursor.execute(query, data)
        record = self.cursor.fetchone()

        if record:
            print(record)
        else:
            print("No record found")

    def delete(self, id):
        query = "DELETE FROM Vehicle WHERE id=%s"
        data = (id,)

        self.cursor.execute(query, data)
        self.conn.commit()

        print("Record deleted successfully")

    def update(self, id, brand, model, type, price, year):
        query = """UPDATE Vehicle
                   SET brand=%s, model=%s, type=%s, price=%s, year=%s
                   WHERE id=%s"""

        data = (brand, model, type, price, year, id)

        self.cursor.execute(query, data)
        self.conn.commit()

        print("Record updated successfully")


v = VehicleListCreateRetrieveUpdateDelete()

v.list()
