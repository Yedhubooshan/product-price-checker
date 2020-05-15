# Amazon-flipkart-Rs-price-checker
A program which checks for price fall below a range and automatically sends mail with link!(My First .py Project)

Note : This app runs for pricing from Rs.100 (hope it works for lakhs and crores)

This program was written with reference from:
  https://www.youtube.com/watch?v=Bg9r_yLk7VY

Requirements:
  1. Python 3  https://www.python.org
  2. Packages: Copy paste the below line to install the packages in one go using cmd (Inside the python app directory)
    pip install requests stdiomask bs4 colorama
    Packages used:
      ->requests : Allows you to send HTTP requests
      ->stdiomask : To mask the password
      ->bs4 : To scrap from Website
      ->colorama : For colors (just for fun)
      ->smtplib : To establish connection and login e-mail
      ->time : To create delay
  3. Check and change for your UserAgent (just google and paste in the code)
 Inputs to be given by the user:
  1. Name of the website (Helps in getting the data from website)
  2. URL of the website
  3. User's mail address
  4. User's Password
  5. Destination mail address
  6. Your Budget
  
Note for Password:(For better Protection)
  ->Enable Two step Authentication
  ->Goto google app passwords
  ->Get 16 digit Password Code
  ->Enter in the input Password
If Lazy: (Less Protection)
	=>Enable Google Less Secure Apps
	=>Enter Your Default Password
  
  Enjoy Buying Stuff!!
