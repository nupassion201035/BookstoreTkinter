from typing import Optional, List
from dataclasses import dataclass, field


@dataclass
class Account:
    id: str
    password: str
    name: str
    email: str
    phone: str

@dataclass
class Admin(Account):
    permission: str = "admin"

@dataclass
class Customer(Account):
    address: str = ""

class System:
    def __init__(self):
        self.admin: List[Admin] = []
        self.customer: List[Customer] = []

    def add_admin(self, admin: Admin):
        self.admin.append(admin)

    def add_customer(self, customer: Customer):
        self.customer.append(customer)
        
    
    
    



server = System()



nut = Customer("nut", "1234", "nut", "email", "phone", "address")
System.add_customer(server , nut)