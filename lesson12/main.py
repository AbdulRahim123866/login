import time

class Car:
     def __init__(self,name ,age,brand,num_wheels,max_speed,is_on):#constructor#implicitly will be writen
         self.name=name
         self.age=age
         self.brand=brand
         self.num_wheels=num_wheels
         self.max_speed=max_speed
         self.is_on=False
         pass

     def start_car(self):
         if self.is_on:
             print(f"{self.name} Car is alreeady running")
         print(f"{self.name} Engine is starting")
         self.is_on=True
         pass

     def drive(self,direction:str="forward"):
         if not self.is_on:
             print(f"{self.name} Start the cat first")
             return
         print(f"{self.name} car is moving {direction}")
         self.is_on = True

     def close(self):
         if not self.is_on:
             print("you cant turn off the car")
             return
         print(f"{self.name} Engine is closing")
         time.sleep(5)
         self.is_on = False
     pass

c1=Car(name="E200",age=2,brand="marcides",num_wheels=4,max_speed=220,is_on=True)
c2=Car(name="dolphine",age=0,brand="BYD",num_wheels=4,max_speed=260,is_on=True)
c3=Car(name="zara",age=8,brand="BMW",num_wheels=4,max_speed=260,is_on=True)

c1.start_car()
c2.drive("bakward")
c2.start_car()
c2.drive()
c3.start_car()
c1.close()
if c2.is_on:
    print(f"{c2.name} is still on...")

for i in [c1,c2]:
    if i.is_on:
        i.close()#validation يعني طفاها بالطريقة المناسبة بردت بعدها طفاها
        i.is_on=False#هاي ما دخل عالفنكشن طفى السيارة مباشرة

    #any change on attributes need to be done using method