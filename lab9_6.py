# Write program to demonstrate constructor channing / constructor overriding

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        print(f"-> Employee Constructor called: Initialized {self.name}")

    def get_details(self):
        return f"Employee [ID: {self.employee_id}, Name: {self.name}]"

class Manager(Employee):

    def __init__(self, name, employee_id, team_size):
        
        # --- Constructor Chaining ---
        super().__init__(name, employee_id) 
        
        self.team_size = team_size
        print(f"-> Manager Constructor called: Initialized team size to {self.team_size}")

    # Overriding the parent's method to include more detail
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Manages Team of {self.team_size} members"

emp1 = Employee("Alex", 1)
manager1 = Manager(emp1.name,emp1.employee_id, 5)