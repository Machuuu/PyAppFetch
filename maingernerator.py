from faker import Faker

fake = Faker()

Names = []

for x in range(0,20):
    Names.append(fake.name())

print(Names)

# dennis is a potatoe