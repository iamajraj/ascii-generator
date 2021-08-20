import requests
from os import system, name

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

def logo():
	logoreq = requests.get(f"https://artii.herokuapp.com/make?text=ASCII")
	logoreq2 = requests.get(f"https://artii.herokuapp.com/make?text=GENERATOR")
	print(bcolors.OKCYAN + logoreq.text)
	print(bcolors.OKGREEN + logoreq2.text)
	print("          AUTHOR:- AJRAJ")
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
logo()
print(bcolors.WARNING + "NOTE:- Internet Connection Required !")
text = input(bcolors.OKGREEN + "Enter Your Text :- \n")
font = input(bcolors.OKCYAN + "Do you want to choose font ? Y/N :- ")
req_font = requests.get("https://artii.herokuapp.com/fonts_list")
if font == "Y" or font == "y":
	print(bcolors.OKGREEN + req_font.text)
	font_name = input("Enter the name of the font correctly :- ")
	req = requests.get(f"https://artii.herokuapp.com/make?text={text}&font={font_name}")
	clear()
else:
	req = requests.get(f"https://artii.herokuapp.com/make?text={text}")
	clear()

result = req.text
print(bcolors.OKGREEN + req.text)

print(bcolors.WARNING + "Do you want to save this ascii ?")
option = input("Y/N:- ")

if option == "Y" or option == "y":
	file = open("ascii.txt", "a")
	file.write("\n")
	file.write(result)
	file.close()
	print(bcolors.OKGREEN + "Saved !")
	exit()
elif option == "N" or option == "n":
	print(bcolors.OKGREEN + "Thanks for using !")
	exit()
else:
	print(bcolors.FAIL + "Invalid option selected")
