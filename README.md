# IONCON Raspberry Pi Control

Create an account in http://iotcon.top/ before installation and copy userid and user hash from API Dashboard

###Installation

Step 1:Connect Raspberry Pi using SSH From Your Computer

Step 2:Install Git ( sudo apt-get install git )

Step 3:Clone the repository ( git clone https://github.com/ramith27/We4u-Raspberry/ )

Step 4 : Change Directory ( cd Raspberry-Control/src ) 

Step 5 : Edit connect.py ( vi connect.py )

Edit 

   user="xxxxxxxxxxx"  //Get userid from api dashboard
   
   hash="xxxxxxxxxxx"  //Get userid from hash dashboard
   
Step 6 : Now run it with root permission 
   sudo python connect.py 

Step 7 : Now you will get tour Raspberry Serial Number (Copy it)

Step 8 : Now add the device in the Dashboard and Enter The Serial Number To Continue

Step 9 : Now you will able to select the port of Raspberry Pi and make a switch for it

Step 10 : Now run connect.py again with root permission and make it as background app using &
   sudo python connect.py &
   
Your installation is done now you will able to control your raspberry from our Dashboard

