import keyboard
import time

from bs4 import BeautifulSoup
import requests

import pyperclip
import os

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

	scriptDirectory = os.path.dirname(__file__)
	javascriptDirectory = os.path.join(scriptDirectory, "ProfileURL.js")
	keyboard.send("f12")
	time.sleep(0.2)
	keyboard.send("ctrl+shift+k")
	time.sleep(0.2)
	with open(javascriptDirectory, "r") as file:
		js_code = file.read()
	pyperclip.copy(js_code)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")

	keyboard.send("alt+d")
	time.sleep(0.2)
	keyboard.send("right arrow")
	time.sleep(0.2)
	keyboard.write("edit/info")
	keyboard.press_and_release("enter")
	time.sleep(3) # Wait for page to load

	keyboard.send("f12")
	time.sleep(0.2)
	keyboard.send("ctrl+shift+k")
	time.sleep(0.2)
	javascriptDirectory = os.path.join(scriptDirectory, "ProfileName.js")
	with open(javascriptDirectory, "r") as file:
		js_code = file.read()
	pyperclip.copy(js_code)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")

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


def GetAllWebsiteLinks(url):
	try:
		response = requests.get(url)
		response.raise_for_status()  # Raise an exception for non-200 status codes

		soup = BeautifulSoup(response.content, 'html.parser')
		links = [link.get('href') for link in soup.find_all('a')]
		
		return links

	except requests.exceptions.RequestException as e:
		print(f"An error occurred while fetching the webpage: {e}")
		return []  # Return an empty list on errors

if __name__ == '__main__':
  main()