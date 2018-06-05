from faker import Faker

fake = Faker()

Names = []
filename = 'output.sql'

for x in range(0,20):
    Names.append(fake.name())

print(Names)

header = 'INSERT INTO PERSON ( ID, NAME ) VALUES '

with open(filename, 'w') as file:
    file.write(header)

    for index, name in enumerate(Names):
        file.write("( " + str(index) + ", " + "\'" + name + "\'" + " )")

        if index != len(Names) - 1:
            file.write(", \n")

# dennis is a potatoe