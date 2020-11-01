from _6_10_1_rectangle import Rectangle
from _6_10_2_rectangle1 import Rectangle1
from _6_10_3_Client_PetShop import Client
from _6_10_4_Classes import EmployeeList, Employee

# ******** Exc 6.10.1 *********
rect = Rectangle(0, 0, 100, 200)
print('******** Exc 6.10.1 *********')
print(rect)
print()

# ******** Exc 6.10.2 *********
rect1 = Rectangle1(100, 200)
print('******** Exc 6.10.2 *********')
print('Rectangle a={0}, b={1}, s={2}'.format(rect1.get_width(), rect1.get_height(), rect1.get_area()))
print()

# ******** Exc 6.10.3 *********
client = Client('Иван', 'Петров', 200)
print('******** Exc 6.10.3 *********')
print(client)
print()

# ******** Exc 6.10.4 *********
elist = EmployeeList()
elist.append(Employee('Иван','Петров','Москва','Наставник'))
elist.append(Employee('Дарья','Петрова','Москва','Волонтер'))
elist.append(Employee('Дмитрий','Иванов','Рязань','Директор'))
print('******** Exc 6.10.4 *********')
print(elist)