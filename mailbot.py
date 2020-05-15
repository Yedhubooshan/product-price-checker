#Hello, Thanks for viewing my first project!Hope its good!! Cheers - Yedhubooshan M M
import requests,smtplib,time,stdiomask
from bs4 import BeautifulSoup
from colorama import init,Fore,Style
init(autoreset=True) #resets color of the text after every line

#getting inputs from user:

print(Fore.YELLOW + Style.BRIGHT + 'Welcome To Amazon/Flipkart India Price Checker!')

website_name= input('amazon/flipkart: ')
if website_name.lower() == 'flipkart':
	print("Flipkart is loading")
elif website_name.lower() == 'amazon':
	print('Amazon is loading')
else:
	print("COME BACK AGAIN AND ENTER PROPERLY!\nBYE!!")
	time.sleep(1.5)
	exit()
URL,login_id,password,dest_mail,min_value= input('Enter URL: '),input('Your E-mail id: '),stdiomask.getpass(),input('Dest_Email: '),int(input('Enter your affordable price: '))
print(Fore.GREEN + Style.BRIGHT +"\nThank you for the providing the required inputs\n"+Fore.CYAN+ Style.BRIGHT +"The indication will be sent to your destination mail when the price falls down\n"+Fore.MAGENTA+ Style.BRIGHT +"Happy Shopping!\n")
print("Check Started !\n")

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
page =  requests.get(URL, headers=headers) #Allows you to send HTTP requests
soup = BeautifulSoup(page.content, 'html.parser') #Getting websites's content
print(Fore.GREEN + Style.BRIGHT + f'Welcome to {website_name}\n')
#getting the product name and price as string
if website_name.lower() == 'flipkart':
	title = soup.find('span', attrs={'class':'_35KyD6'}).get_text() #Getting product title
	price = soup.find('div', attrs={'class':'_1vC4OE _3qQ9m1'}).get_text() #Getting product price
	cprice=price[1:9] #getting string of the price!
	print(title,cprice)

elif website_name.lower() == 'amazon':
	title = soup.find(id='productTitle').get_text() #Getting product title
	price = soup.find(id='priceblock_ourprice').get_text() #Getting product price
	cprice=price[2:10] 
	print(title.strip(),'Rs.'+cprice+'\n')
else:
	print('Learn the name of website and come again!\nBYE!!')
	time.sleep(2)
	exit()
	
def check_price():

	#Extracting Price Value from Text
	final_price=[]
	for i in range(len(cprice)):
		if cprice[i] !='.':
			if cprice[i].isnumeric():
				final_price.append(cprice[i])
		else:
			break;
	final_price=int(''.join(final_price))
	print(Fore.YELLOW+ Style.BRIGHT +'Current Price:',Fore.CYAN + Style.BRIGHT + str(final_price))
	#Displaying Date & Time
	hour=int(time.strftime('%H'))
	if hour>11:
		if hour != 12:
			hour -= 12
		print (Fore.MAGENTA + Style.BRIGHT + time.strftime("Date: %D, Time: "+str(hour)+":%M:%S PM\n"))
	else:
		print (Fore.MAGENTA + Style.BRIGHT + time.strftime("Date: %D, Time: "+str(hour)+":%M:%S AM\n"))
	#Checking Price Condition
	if final_price<=min_value:
		send_email()
		return 1
	else:
		print(Fore.RED + Style.BRIGHT + "EMAIL NOT SENT !\n")
		return 0
#Sending mail function		
def send_email():
	
	#Server Connection Extablishment
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	#Logging into User's Mail
	server.login(login_id,password)
	#Content of the mail
	subject = 'Lookout out the price drop :-)'
	body= f'Checkout the {website_name} link:\n' + URL
	msg = f'subject:{subject}\n\n{body}'

	#Sending mail
	#User mail id,Destination mail id,mail message
	server.sendmail(login_id,dest_mail,msg)
	print(Fore.GREEN + Style.BRIGHT + "EMAIL SENT !\n")
	time.sleep(5)
	#Logging out User's Mail
	server.quit()

#Calling Function
check_bit=0
while check_bit==0 :
	check_bit=check_price()
	if check_bit==1:
		print('BYE!!')
		time.sleep(2)
		exit()
	else:
		time.sleep(60)
