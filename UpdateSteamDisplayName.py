import keyboard
import time

from bs4 import BeautifulSoup
import requests

import json
import pyperclip
import os
import test

def main():
	newName = "Json"

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
	keyboard.send("f12")
	time.sleep(0.5)
	keyboard.send("ctrl+shift+k")
	time.sleep(0.5)
	jsonDirectory = os.path.join(scriptDirectory, "JavascriptCommands.json")
	with open(jsonDirectory) as json_file:
		jsonData = json.load(json_file)
	profileUrlJsCode = jsonData["ProfileURL"]
	profileUrlJsCode = "\n".join(profileUrlJsCode)
	pyperclip.copy(profileUrlJsCode)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")
	time.sleep(3) # Wait for page to load

	keyboard.send("f12")
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
	profileNameJavascript = GetProfileNameJavascript(newName)
	pyperclip.copy(profileNameJavascript)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")
	time.sleep(0.2)
	saveProfileJsCode = jsonData["SaveProfileEdit"]
	saveProfileJsCode = "\n".join(saveProfileJsCode)
	pyperclip.copy(saveProfileJsCode)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")

	keyboard.send("ctrl+w")

def GetProfileNameJavascript(newName):
	profileNameJavascript = [
		"const inputElement = document.querySelector(\"div.DialogInputLabelGroup:nth-child(1) > label:nth-child(1) > div:nth-child(2) > input:nth-child(1)\");",
		"if (inputElement) {",
		"  const inputValue = inputElement.value;",
		"  console.log(\"The current value in the input element is:\", inputValue);",
		"  inputElement.value = \"" + newName + "\";",
		"} else {",
		"  console.error(\"Input element not found with the provided CSS selector.\");",
		"}"
	]

	profileNameJavascript = "\n".join(profileNameJavascript)

	return profileNameJavascript

if __name__ == '__main__':
  main()