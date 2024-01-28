import keyboard
import time

from bs4 import BeautifulSoup
import pyperclip
import requests

def main():
	newName = "JohnIsMyName"
    
	keyboard.send("win")
	time.sleep(0.2)
	keyboard.write("Firefox") # Update this line for a different browser
	time.sleep(0.2)
	keyboard.press_and_release("enter")
	time.sleep(3) # Wait for page to load

	steamURL = "https://steamcommunity.com"
	keyboard.send("alt+d")
	keyboard.write(steamURL)
	keyboard.press_and_release("enter")
	time.sleep(3) # Wait for page to load

	LoopTabbing(timesToLoop=2)
	keyboard.press_and_release("enter")
	time.sleep(1) # Wait for page to load

	keyboard.send("alt+d")
	time.sleep(0.2)
	keyboard.send("right arrow")
	time.sleep(0.2)
	keyboard.write("edit/info")
	keyboard.press_and_release("enter")
	time.sleep(3) # Wait for page to load

	# The commented out code is meant to act as a dynamic way to find the Profile Name field. 
	# Currently we are looping a certain amount of times, however this is not good practice as what if the amount of options changes
	'''keyboard.send("alt+d")
	time.sleep(1)
	keyboard.send("ctrl+c")
	time.sleep(1)
	editProfileURL = pyperclip.paste()
	request = requests.get(editProfileURL)
	webpageHTML = BeautifulSoup(request.text, 'html.parser')
	for link in webpageHTML.find_all('input'):
		print(link.get('href'))
		currentURL = link.get('href')
		if "https://steamcommunity.com/id/" in currentURL:
			keyboard.send("alt+d")
			keyboard.write(currentURL)
			break'''

	LoopTabbing(timesToLoop=39)
	keyboard.send("ctrl+a")
	keyboard.write(newName)
	time.sleep(1) # Wait for page to load

	LoopTabbing(timesToLoop=7)
	keyboard.press_and_release("enter")
	time.sleep(1) # Wait for page to load

	keyboard.send("ctrl+w")

def LoopTabbing(timesToLoop):
	for iteration in range(timesToLoop):
		keyboard.send("tab")

if __name__ == '__main__':
  main()