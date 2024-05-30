print("hello")
print("thankyou")
class Car:
    
    def __init__(self,brand,model,year,fuel_type,CC,price,features,wheel_drive):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.CC = CC
        self.price = price
        self.features = features
        self.is4wd = wheel_drive
    
        
    def car_info(self):
        print("Car_info")
        print("Brand :",self.brand)
        print("Model :",self.model)
        print("Manufacture Year :",self.year)
        print("Fuel type :",self.fuel_type)
        print("Engine capacity :", "{}".format(self.CC)+ ("cc" if self.fuel_type != "electric" else "KWH"))
        print("Price :",self.price)
        print("Features :",self.features)
        print("wheel drive : 4WD") if self.is4wd == True else print("wheel drive : 2WD")
        
list_cars = [ ]   

car = Car("Toyota","Innova",2001,"petrol",2.4,3000000,["2 Airbags","Sunroof"],False)
car.car_info()
list_cars.append(car)

car = Car("TATA","safari",2004,"diesel",2.5,1800000,["6 Airbags","LCD screen"],True)
car.car_info()
list_cars.append(car)

car = Car("Ford","Endeavour",2023,"petrol",3.0,2500000,["6 Airbags","Sunroof"],True)
car.car_info()
list_cars.append(car)

car = Car("KIA","Seltos",2022,"petrol",1.5,1800000,["2 Airbags","Sunroof"],False)
car.car_info()
list_cars.append(car)

car = Car("BMW","M5",2024,"petrol",4.0,10000000,["8 Airbags","ADAS"],True)
car.car_info()
list_cars.append(car)

car = Car("Hyundai","Kona",2022,"electric",64,2300000,["6 Airbags","359L Bootspace"],False)
car.car_info()
list_cars.append(car)

print(list_cars)

for car in list_cars:
    if car.year >= 2020:
        print(car.model)

for car in list_cars:
    if "Sunroof" in car.features or "6 Airbags" in car.features:
        print(car.model)


print(list_cars)


car1 = [ ]
car2 = [ ]

for car in list_cars:
    AB_count = 0
    
    for feature in car.features:
        if "Airbags" in feature:
            AB_count = int(feature.split()[0])
                
                   
    if car.is4wd == True and AB_count >= 4 and ((car.fuel_type == "petrol" and car.CC >= 3.0) or (car.fuel_type == "diesel" and car.CC >= 2.0)):
        
        car1.append(car.model)
    else:
        car2.append(car.model)

print("Safe cars :",car1)
print('Unsafe cars:',car2) 

lsit = [ ]
for car in list_cars:
    lsit.append(car.features[0])
    
lsit = [int(num.split()[0])for num in lsit]
print(lsit)

grt_four = [num for num in lsit if num >= 4]
print(grt_four)

print(car.price)

print(car.model)

x = ["vamsi","vijay"]
x.insert(1,"ravi")
print(x)

x = ["vamsi","vijay"]
y = ["ravi"]
x.insert(2,y)
print(x)
x.pop(1)
print(x)

x = ['vamsi', 'ravi', 'vijay']
x.remove("vamsi")
print(x)

x = ['vamsi', 'ravi', 'vijay']
y = {"rajesh":24}
x.append(y)
print(x)

file = open('demo_text.txt', 'r')

for each in file:
    print(each)

with open("demo_text.txt")as file:
    data = file.read()

print(data)

file = open("demo_text.txt","r")
print(file.read(5))


file = open("demo_text.txt",'w')
file.write("writing a command line ")
file.write(" accessing files ")
file.close()

file = open('demo_text.txt','a')
file.write('  line has been added')
file.close()

file = open('demo_text.txt','r')

print(file.readlines())

file = open("sampledownload.jpeg","rb")
file2 = open("mypic.JPG","wb")
for i in file:
    file2.write(i)

file3 = open("myfile.txt","a")

file3.write(" company \n")
file3.write(" model \n")
file3.write(" year \n")
file3.write(" created a log ")
file3.close()

import os

os.remove("myfile.txt")

import os

def create_file(filename):
    try:
        with open(filename, "w") as file:
                  file.write("hello,world!\n")
        print("file " + filename + "created successfully.")
    except IOError:
        print()

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except IOError:
        print("error: could not read file " + filename)

def append_file(filename, text):
    try:
        with open(filename, "a") as file:
            file.write(text)
            print("text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)
              
def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)
 
def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)

if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"
 
    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)

a = 2
b = 0
try:
    print(a/b)
except Exception:
    print("numbers cannot be divided")


file = open("vamsi's.txt","a")

file.write("info \n")
file.write("Name \n")
file.write("Date of birth \n")
file.write("Place of birth \n")
