import json
import jsonpickle
from typing import List
import sqlite3
from sqlite3 import Connection
from pyldes_kbo.models.kbo_enterprise import \
    KboEnterprise, \
    KboCode, \
    KboContact, \
    KboActivity, \
    KboAddress, \
    KboDenomination, \
    KboEstablishment


class KboGenerator ():

    def __init__(self, base_path: str, db_location:str):
        self.base_path = base_path
        self.db_location = db_location

    def count(self) -> int:
        print(self.db_location)
        conn = sqlite3.connect(self.db_location)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM enterprise")
        num_rows = (cursor.fetchone())[0]
        return num_rows

    def generate(self):
        conn = sqlite3.connect(self.db_location)
        cursor = conn.cursor()
        # use batch processing 
        offset = 0
        limit = 100
        cursor.execute(f"SELECT * FROM enterprise LIMIT {limit} OFFSET {offset}")
        enterprise_rows = cursor.fetchall()
        while len(enterprise_rows) > 0:
            for enterprise_row in enterprise_rows:
                enterprise = self.get_enterprise(enterprise_row)
                yield enterprise
            offset += limit
            cursor.execute(f"SELECT * FROM enterprise LIMIT {limit} OFFSET {offset}")
            enterprise_rows = cursor.fetchall()
        # Close the connection
        conn.close()

    def one(self, enterprise_nr:str) -> KboEnterprise:
        # print(self.db_location)
        conn = sqlite3.connect(self.db_location)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM enterprise WHERE EnterpriseNumber=?", (enterprise_nr,))
        enterprise_row = cursor.fetchone()
        enterprise = self.get_enterprise(enterprise_row)
        conn.close()
        return enterprise

    def get_enterprise(self, enterprise_record) -> KboEnterprise:
        enterprise = KboEnterprise()
        enterprise.enterprise_number = enterprise_record[1]
        conn = sqlite3.connect(self.db_location)
        enterprise.status = self.get_code(conn, "Status", enterprise_record[2])
        enterprise.juridical_situation = self.get_code(conn, "JuridicalSituation", f"{enterprise_record[3]:03d}")
        enterprise.type_of_enterprise = self.get_code(conn, "TypeOfEnterprise", enterprise_record[4])
        enterprise.juridical_form = self.get_code(conn, "JuridicalForm", f"{int(enterprise_record[5]):03d}")
        enterprise.start_date = enterprise_record[7]
        enterprise.activities = self.get_activities(conn, enterprise.enterprise_number)
        enterprise.contacts = self.get_contacts(conn, enterprise.enterprise_number)  
        enterprise.addresses = self.get_addresses(conn, enterprise.enterprise_number)
        enterprise.denominations = self.get_denominations(conn, enterprise.enterprise_number)
        enterprise.establishments = self.get_establishments(conn, enterprise.enterprise_number)
        conn.close()
        return enterprise

    code_cache = {}
    def get_code(self, conn: Connection, catgeory: str, code: str) -> KboCode:
        cache_key = f"{catgeory}-{code}"
        if cache_key in KboGenerator.code_cache:
            return KboGenerator.code_cache[cache_key]
        # get from db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM code WHERE category=? AND code=?", (catgeory, code))
        code_rows = cursor.fetchall()
        kbo_code = KboCode()
        kbo_code.category = catgeory
        kbo_code.code = code
        kbo_code.descriptions = {}
        for code_row in code_rows:
            kbo_code.descriptions[code_row[3]] = code_row[4]
        # add to cache and return
        KboGenerator.code_cache[cache_key] = kbo_code
        return kbo_code

    def get_activities(self, conn: Connection, entity_nr: str) -> List[KboActivity]:
        activities = []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM activities WHERE EntityNumber=?", (entity_nr, ))
        activity_rows = cursor.fetchall()
        for activity_row in activity_rows:
            activity = KboActivity()
            activity.activity_group = self.get_code(conn, 'ActivityGroup', activity_row[2])
            activity.nace_version = activity_row[3]
            activity.nace_code = self.get_code(conn, f'Nace{activity_row[3]}', activity_row[4])
            activity.classification = self.get_code(conn, 'Classification', activity_row[5])
            activities.append(activity)
        return activities
    
    def get_addresses(self, conn: Connection, entity_nr: str) -> List[KboAddress]:
        addresses = []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM address WHERE EntityNumber=?", (entity_nr, ))
        address_rows = cursor.fetchall()
        for address_row in address_rows:
            address = KboAddress()
            address.type_of_address = self.get_code(conn, 'TypeOfAddress', address_row[2])
            address.zip_code = address_row[5]
            address.municipality = address_row[6]
            address.street = address_row[8]
            address.house_number = address_row[10]
            address.box = address_row[11]
            address.extra_info = address_row[12]
            address.full_address = address_row[8]+" "+address_row[10]+", "+address_row[5]+" "+address_row[6]+", "+"Belgium"
            address.full_address_no_bracket = ((address_row[8].partition('(')[0]).replace("Bld ", "Boulevard " )).partition(',')[0]+" "+address_row[10]+", "+address_row[5]+" "+address_row[6].partition('(')[0]+", "+"Belgium"
            addresses.append(address)
        return addresses
    
    def get_denominations(self, conn: Connection, entity_nr: str) -> List[KboDenomination]:
        denominations = []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM denomination WHERE EntityNumber=?", (entity_nr, ))
        denom_rows = cursor.fetchall()
        for denom_row in denom_rows:
            denom = KboDenomination()
            denom.language = self.get_code(conn, 'Language', denom_row[2])
            denom.type_of_denomination = self.get_code(conn, 'TypeOfDenomination', f'{denom_row[3]:03d}')
            denom.denomination = denom_row[4]
            denominations.append(denom)
        return denominations

    def get_establishments(self, conn: Connection, enterprise_nr: str) -> List[KboEstablishment]:
        establishments = []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM establishment WHERE EnterpriseNumber=?", (enterprise_nr, ))
        est_rows = cursor.fetchall()
        for est_row in est_rows:
            establishment = KboEstablishment()
            establishment.estblishment_number = est_row[1]
            establishment.addresses = self.get_addresses(conn, establishment.estblishment_number)
            establishment.contacts = self.get_contacts(conn, establishment.estblishment_number)
            establishment.start_date = est_row[2]
            establishment.enterprise_number = est_row[3]
            establishments.append(establishment)
        return establishments

    def get_contacts(self, conn: Connection, entity_nr: str) -> List[KboContact]:
        contacts = []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contact WHERE EntityNumber=?", (entity_nr, ))
        contact_rows = cursor.fetchall()
        for contact_row in contact_rows:
            contact = KboContact()
            contact.entity_contact = self.get_code(conn, 'EntityContact', contact_row[2])
            contact.contact_type = self.get_code(conn, 'ContactType', contact_row[3])
            contact.value = contact_row[4]
            contacts.append(contact)
        return contacts