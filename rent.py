# Project rentel agency --- car rentel project
import pickle
try:
    import sqlite3
    cann=sqlite3.connect("mydata.db")
    cur=cann.cursor()
    data="CREATE TABLE rentle_cars (total_cars int DEFAULT 00,number_days int,name varchar(30),address varchar(255),phone varchar(20),adhar int PRIMARY KEY,Total_bill int,deposit_cars int,remaining_cars int,final int)"
    cann.execute(data)
    cann.commit()
except:
    pass
     # print("Data base already created ")

print("""
        M-S Rentle Car Agency
        Uttrakhand Dehradun
        Contact number- 7065593283
""")
import sqlite3
cann=sqlite3.connect("mydata.db")
cur=cann.cursor()
data2="SELECT sum(final) FROM rentle_cars "
output=cann.execute(data2)
output1=0
for i in output:
    output1=(i[0])
    # print(output1)
    if output1 is None:
        output1=0
        print(output1)
availbale_cars = 50
print("Availbale cars :",availbale_cars-output1)
new_avaibale=availbale_cars-output1
print()
d=(f"""
    1-Cars Rent
    2-Cars deposit
    3-Exit

We have total available car {availbale_cars-output1} only //
""")
print(d)
user=int(input("Pleae choose :"))
if user==1:
    print("Please note - 1 car will be 5000 charges for 1 day")
    user1 = input("Are you confortable: yes or no :")
    if user1.lower()=="yes":
        total_cars=int(input("Total number of cars :"))
        total_cars2=total_cars
        if total_cars<=new_avaibale and new_avaibale>=0:
            number_days=int(input("Total number of days :"))
            name=input("Your name please :")
            address=input("Your address please :")
            phone=input("Your phone number please :")
            adhar=input("Your id :")
            Total_bill=total_cars*5000
            print("Your total bill is ",Total_bill )
            conformation=input("Please confrim  - Yes/No ")

            if conformation.lower()=="yes":
                print("Your booking has been successfully confrim Below are details kindly confrim once :")
                print(f"""
                name :{name}
                total cars :{total_cars}
                number of days :{number_days}
                id  :{adhar}
                total bill : {Total_bill}
                Booking confrim
                """)

                # Crete a text file to print the invoice

                p=open(f"{adhar}.txt","w")
                p.write(f"""
                Your total cars is --{total_cars}
                Your id -- {adhar}
                Your total amunt is --{Total_bill}
                Thanks 
                """)
                p.close


                # Store the data in sqlite3
                try:
                    import sqlite3
                    cann = sqlite3.connect("mydata.db")
                    cur = cann.cursor()
                    data2="INSERT INTO rentle_cars VALUES (?,?,?,?,?,?,?,?,?,?)"
                    t=(total_cars ,number_days ,name ,address ,phone ,adhar ,Total_bill,0,0,total_cars2)
                    cur.execute(data2,t)
                    cann.commit()
                    cann.close()
                except:
                    print("Given id is already there :")

            else:
                pass

        else:
            print()
            print()
            print(f"Dear customer you need to choose lesser car count, Because we have only 50 cars")
    else:
        pass

# Second part start here--- for deposit the cars
elif user==2:
    print("Please entre your id so that we can find your details :")
    id=int(input("entre id :"))
    print()
    print("""Please Note: If you are deposit cars for the second time, please enter the total number of cars :""")
    cars = int(input("Number's of cars :"))

    # Find the value of cars
    import sqlite3

    cann = sqlite3.connect("mydata.db")
    cur = cann.cursor()
    t = (cars, id)
    data = ("SELECT total_cars FROM rentle_cars where adhar=?")
    t=(id,)
    main=0
    quary=cur.execute(data, t)
    for i in quary:
        main=i[0]
    cann.commit()

    # Update the value in the data base

    import sqlite3
    cann=sqlite3.connect("mydata.db")
    cur=cann.cursor()
    t=(cars,id)
    t1=(cars,id)
    new = (main - cars)
    t2=(new,id)
    if cars<=int(main):

        # data=("UPDATE rentle_cars SET total_cars=? where adhar=?")
        data2 = ("UPDATE rentle_cars SET deposit_cars=? where adhar=?")
        data3 = ("UPDATE rentle_cars SET remaining_cars=? where adhar=?")
        data1 = ("UPDATE rentle_cars SET final=? where adhar=?")

        cur.execute(data1, t2)
        cur.execute(data2, t1)
        cur.execute(data3, t2)
        cann.commit()
        print("Your remainig cars ",main-cars)

elif user==3:
    # print("Program finish ,Please try agian ")
    pass

print("Program finish")










