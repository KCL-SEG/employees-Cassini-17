"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=None, hours=None,hourly_wage=None, commission=None, fixed_bonus=None, contracts_landed=None, contract_wage=None):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.hourly_wage = hourly_wage
        self.commission = commission
        self.fixed_bonus = fixed_bonus
        self.contracts_landed = contracts_landed
        self.contract_wage = contract_wage

    def get_contract_info(self):
        total = 0
        description = "works on a "

        if self.salary:
            total += self.salary
            description += f"monthly salary of {self.salary}"

        if self.hours and self.hourly_wage:
            total += self.hours * self.hourly_wage
            description += f"contract of {self.hours} hours at {self.hourly_wage}/hour"

        if self.commission and self.fixed_bonus:
            total += self.fixed_bonus
            description += f" and receives a bonus commission of {self.fixed_bonus}"

        if self.commission and self.contracts_landed and self.contract_wage:
            total += self.contracts_landed * self.contract_wage
            description += f" and receives a commission for {self.contracts_landed} contract(s) at {self.contract_wage}/contract"

        description += f". Their total pay is {total}."
        return (total, description)

    def get_pay(self):
        contract_info = self.get_contract_info()
        total_pay = 0
        return contract_info[total_pay]


    def __str__(self):
        contract_info = self.get_contract_info()
        description = 1
        return f"{self.name} " + contract_info[description]


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, hourly_wage=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, commission=True, contracts_landed=4, contract_wage=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_wage=25, commission=True, contracts_landed=3, contract_wage=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, commission=True, fixed_bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourly_wage=30, commission=True, fixed_bonus=600)


