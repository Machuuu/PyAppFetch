from faker import Faker

fake = Faker()

Names = ["" for x in range(20)]

for x in range(0,20):
    Names[x] = fake.name()

print(Names)
