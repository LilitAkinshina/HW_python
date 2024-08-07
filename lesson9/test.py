from api import EmployeeApi
from DataBase import CompanyTable
from DataBase import EmployeeTable


base_url = 'https://x-clients-be.onrender.com'
employee_api = EmployeeApi(base_url)

db_connection_string = ('postgresql://x_clients_db_3fmx_user:'
                        'mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@'
                        'dpg-cour99g21fec73bsgvug-a.oregon-postgres.'
                        'render.com/x_clients_db_3fmx')
company_table = CompanyTable(db_connection_string)
employee_table = EmployeeTable(db_connection_string)

# Новая компания
name = 'NewCompany4'
description = 'My new company 4'

# Новый сотрудник
id = 1
first_name = "Lilit"
last_name = "Akinshina"
middle_name = "Anatolyevna"
email = "new@gmail.com"
employee_url = "url1.com"
phone = "89999999999"
birthdate = "2000-06-07T08:06:30.137Z"
is_active = True


def test_get_employee_list():
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()
    employee_list_api = employee_api.get_employee_list(new_company_id)
    employee_list_db = employee_table.get_company_employees(new_company_id)
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)
    assert employee_list_api[0]["id"] == new_employee_id, \
        "Employee's ID is not equal"
    assert len(employee_list_api) == len(employee_list_db)


def test_create_employee():
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()
    new_employee = employee_api.add_employee(id, first_name, last_name,
                                             middle_name, new_company_id,
                                             email, employee_url, phone,
                                             birthdate, is_active)
    new_employee_id = new_employee["id"]
    employee = employee_table.get_employee_by_id(new_employee_id)
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert len(employee) == 1, "Employee was not created"


def test_get_employee():
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()
    employee = employee_api.get_employee(new_employee_id)
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert employee["id"] == new_employee_id
    assert employee["firstName"] == first_name
    assert len(employee) == 12


def test_change_employee_by_api():
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()
    new_email = "new_new@gmail.com"
    new_url = "url2.com"
    new_is_active = False
    patched_employee = employee_api.patch_employee(new_employee_id,
                                                   new_email, new_url,
                                                   new_is_active
                                                   )
    assert patched_employee["id"] == new_employee_id
    assert patched_employee["email"] == new_email
    assert patched_employee["url"] == new_url
    assert patched_employee["isActive"] == new_is_active
    employee = employee_table.get_employee_by_id(new_employee_id)
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert employee[0][0] == new_employee_id
    assert employee[0][8] == new_email
    assert employee[0][10] == new_url
    assert employee[0][1] == new_is_active


def test_change_employee_by_db():
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()
    new_email = "new_new@gmail.com"
    new_url = "url2.com"
    new_is_active = False
    employee_table.update(new_employee_id, new_email, new_url, new_is_active)
    employee = employee_api.get_employee(new_employee_id)
    assert employee["id"] == new_employee_id
    assert employee["email"] == new_email
    assert employee["avatar_url"] == new_url
    assert employee["isActive"] == new_is_active