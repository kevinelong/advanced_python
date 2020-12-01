import json
from json import JSONEncoder


class Employee:
    def __init__(self, name, salary, employee_address):
        self.name = name
        self.salary = salary
        self.address = employee_address
        self.is_manager = False


class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin


# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


address = Address("Columbia City", "1750 6TH ST", "97018")
employee = Employee("Kevin", 9000, address)

print(EmployeeEncoder().encode(employee))

employeeJSONData = json.dumps(employee, indent=4, cls=EmployeeEncoder)
print(employeeJSONData)

employeeJSON = json.loads(employeeJSONData)
print(employeeJSON)
