from sqlalchemy import create_engine
from sqlalchemy.sql import text


class EmployeeTable:
    scripts = {
        "delete employee": text("DELETE FROM employee "
                                "WHERE id = :new_employee_id"),
        "get company's employees": text("SELECT * FROM employee "
                                        "WHERE company_id = :company_id"),
        "get employee by id": text("SELECT * FROM employee "
                                   "WHERE id = :employee_id"),
        "get max id": text("SELECT MAX(id) FROM employee"),
        "insert new": text("INSERT INTO employee(first_name, last_name, "
                           "phone, company_id, is_active) "
                           "VALUES (:first_name, :last_name, :phone, "
                           ":company_id, :is_active)"),
        "update employee": text("UPDATE employee "
                                "SET email = :new_email, "
                                "avatar_url = :new_url, "
                                "is_active = :new_is_active "
                                "WHERE id = :new_employee_id")
    }

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

    def create(self, first_name, last_name, phone, company_id, is_active):
        new_employee = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "company_id": company_id,
            "is_active": is_active
        }
        self.db.execute(self.scripts["insert new"], new_employee)

    def delete(self, id):
        self.db.execute(self.scripts["delete employee"], new_employee_id=id)

    def get_company_employees(self, new_company_id):
        return self.db.execute(self.scripts["get company's employees"],
                               company_id=new_company_id).fetchall()

    def get_employee_by_id(self, id):
        return self.db.execute(self.scripts["get employee by id"],
                               employee_id=id).fetchall()

    def get_max_id(self):
        return self.db.execute(self.scripts["get max id"]).fetchall()[0][0]

    def update(self, id, email, url, is_active):
        self.db.execute(self.scripts["update employee"], new_email=email,
                        new_url=url, new_is_active=is_active,
                        new_employee_id=id)


class CompanyTable:
    __scripts = {
        "select": 'select * from company where deleted_at is null',
        "select_only_active": 'select * from company '
                              'where deleted_at is null '
                              'and is_active = true',
        "delete_by_id": text("DELETE FROM company WHERE id = :id_to_delete"),
        "insert new": text("INSERT INTO company(\"name\", description) "
                           "VALUES (:new_name, :new_description)"),
        "get_max_id": text("SELECT MAX(id) FROM company"),
        "select_by_id": text('SELECT * FROM company '
                             'WHERE id = :select_id '
                             'AND deleted_at is null')
    }

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

    def delete(self, id):
        self.db.execute(self.__scripts["delete_by_id"], id_to_delete=id)

    def create(self, name, description):
        self.db.execute(self.__scripts["insert new"], new_name=name,
                        new_description=description)

    def get_max_id(self):
        return self.db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]
