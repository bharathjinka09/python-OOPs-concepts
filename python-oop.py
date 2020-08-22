# Inheritance
class User:
	def log(self):
		print('Users')

# Polymorphism
class Teacher(User):
	def log(self):
		print("I'm a teacher!")

class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    # getters and setters (Abstraction -> give output result instead of showing the internal functionality)
    @property
    def name(self):
        print('getting name...')
        return self._name  # _ = private

    @name.setter
    def name(self, name):
        print('setting name...')
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def log(self):
    	print("I'm a customer")

    def update_membership(self, new_membership):
        print('calculating costs....')
        self.membership_type = new_membership

    def read_customer():
        print('Reading customer from db....')

    def __str__(self):
        return f"{self.name} {self.membership_type}"

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    # comparing two customers
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    __hash__ = None

    __repr__ = __str__

# c = Customer('bharath', 'gold')
# print(c.name, c.membership_type)

# c2 = Customer('ram', 'bronze')
# print(c2.name, c2.membership_type)


customers = [Customer('bharath', 'gold'),
             Customer('ram', 'bronze')]

# compare two customers
print(customers[0] == customers[1])

print(customers)

# prints all customers with __str__ format
Customer.print_all_customers(customers)

# print(customers[0].name, customers[0].membership_type)
# print(customers[1].name, customers[1].membership_type)

# print(customers[1].membership_type)
# customers[1].update_membership('gold')
# print(customers[1].membership_type)

# Customer.read_customer()

# __str__ will call here
# print(customers[1])

# del customers[0].name
print(customers[0].name)


# inheritance

customers[0].log()

# Polymorphism
users = [Customer('bharath', 'gold'),
             Customer('ram', 'bronze'),
             Teacher()]

for user in users:
	user.log()