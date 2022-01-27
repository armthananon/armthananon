class Product:
  def __init__(self, name, brand, size, price, stock):
    self.name = name
    self.brand = brand
    self.size = size
    self.price = price
    self.stock = stock

class Employee:
  def __init__(self, id, name, age, address, position):
    self.id = id
    self.name = name
    self.age = age
    self.address = address
    self.position = position

class Customer:
  def __init__(self, id, name, address, phone):
    self.id = id
    self.name = name
    self.address = address
    self.phone = phone

P001 = Product('chair','LIDKULLEN','60x60x70cm',790,100)
P002 = Product('table','TROTTEN','60x120x75cm',1990,30)
P003 = Product('wardrobe','RAKKESTAD','79x55x175cm',3290,20)
P004 = Product('shelf','JONAXEL','50x51x70cm',1090,200)

Em01 = Employee('001','Somrak',32,'Bangna','manager')
Em02 = Employee('002','Sarawut',28,'Ladkrabang','cashier')

C001 = Customer('1001','Chaiya','Rangsit','0823456789')
C002 = Customer('1002','Noppadon','Bangjak','0987654321')


print(P001.price)
P001.price = 500
print(Em01.name)
Em01.name = 'Somsuk'
print(C001.phone +'\n')
C001.phone = '0972567117'

print(P001.price)
print(Em01.name)
print(C001.phone)
