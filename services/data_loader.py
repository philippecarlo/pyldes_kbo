"""
Module data_loader.py
"""
import os
from typing import List
import sqlite3
import pandas

class DataLoader():
    """
    Class to load CSV data from KBO into a SQLite database.
    """

    def __init__(self, base_path: str, kbo_version: str, db_location:str):
        """
        Initialize the class by building the proper paths for all files.
        """
        self.base_path = base_path
        self.kbo_version = kbo_version
        self.db_location = db_location
        self.activities=os.path.join(self.base_path, self.kbo_version, 'activity.csv')
        self.address=os.path.join(self.base_path, self.kbo_version, 'address.csv')
        self.branch=os.path.join(self.base_path, self.kbo_version, 'branch.csv')
        self.code=os.path.join(self.base_path, self.kbo_version, 'code.csv')
        self.contact=os.path.join(self.base_path, self.kbo_version, 'contact.csv')
        self.denomination=os.path.join(self.base_path, self.kbo_version, 'denomination.csv')
        self.enterprise=os.path.join(self.base_path, self.kbo_version, 'enterprise.csv')
        self.establishment=os.path.join(self.base_path, self.kbo_version, 'establishment.csv')
        self.meta=os.path.join(self.base_path, self.kbo_version, 'meta.csv')

    def load_data(self):
        """
        Load the different CSV files into the database
        """
        self.load_csv(self.code, "code")
        self.load_csv(self.activities, "activities", "EntityNumber")
        self.load_csv(self.enterprise, "enterprise", "EnterpriseNumber")
        self.load_csv(self.establishment, "establishment", "EnterpriseNumber")
        self.load_csv(self.address, "address", "EntityNumber")
        self.load_csv(self.contact, "contact", "EntityNumber")
        self.load_csv(self.denomination, "denomination", "EntityNumber")
    
    def load_csv(self, filename: str, tablename: str, index_columns=List[str]):
        """
        Loads a single CSV file into the database.
        Also creates any indexes required to speed up querying.
        """
        print(f"Loading file '{filename}' into table '{tablename}'.")
        data = pandas.read_csv(filename)
        data.columns = data.columns.str.strip()
        conn = sqlite3.connect(self.db_location)
        data.to_sql(tablename, conn, if_exists='replace')
        if index_columns is not None:
            cursor = conn.cursor()
            for ix_column in index_columns:
                cursor.execute(f"CREATE INDEX ix_{tablename}_{ix_column} ON {tablename} ({ix_column});")
        conn.close()