from filemanager import FileManager
from car import Car

filemanager = FileManager("cars.txt")
file_output = filemanager.get_line_number(5)
print(file_output)

print("===========")
car_type = file_output
car = Car(car_type)
car.display_type()
