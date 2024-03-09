import keyboard
import json
import pyperclip
import os
import time

NEW_DISPLAY_NAME = "other"

def main():
	OpenBrowser("Firefox")
	OpenSteamWebpage()

	scriptDirectory = os.path.dirname(__file__)
	jsonDirectory = os.path.join(scriptDirectory, "JavascriptCommands.json")
	with open(jsonDirectory) as json_file:
		jsonData = json.load(json_file)

	OpenSteamProfile(jsonData)
	OpenProfileEdit()
	EditProfileName()
	SaveProfileEdits(jsonData)

	keyboard.send("ctrl+w")

def OpenBrowser(browser):
	keyboard.send("win")
	time.sleep(0.2)
	keyboard.write(browser)
	time.sleep(0.2)
	keyboard.press_and_release("enter")
	time.sleep(3)

def OpenSteamWebpage():
	steamURL = "https://steamcommunity.com"
	keyboard.send("alt+d")
	keyboard.write(steamURL)
	keyboard.press_and_release("enter")
	time.sleep(3)

def OpenSteamProfile(jsonData):
	keyboard.send("f12")
	time.sleep(0.5)
	keyboard.send("ctrl+shift+k")
	time.sleep(0.5)
	profileUrlJsCode = jsonData["ProfileURL"]
	profileUrlJsCode = "\n".join(profileUrlJsCode)
	pyperclip.copy(profileUrlJsCode)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")
	time.sleep(3)

def OpenProfileEdit():
	keyboard.send("f12")
	keyboard.send("alt+d")
	time.sleep(0.2)
	keyboard.send("right arrow")
	time.sleep(0.2)
	keyboard.write("edit/info")
	keyboard.press_and_release("enter")
	time.sleep(3)

def EditProfileName():
	keyboard.send("f12")
	time.sleep(0.2)
	keyboard.send("ctrl+shift+k")
	profileNameJavascript = GetProfileNameJavascript(NEW_DISPLAY_NAME)
	pyperclip.copy(profileNameJavascript)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")
	time.sleep(0.2)

def SaveProfileEdits(jsonData):
	saveProfileJsCode = jsonData["SaveProfileEdit"]
	saveProfileJsCode = "\n".join(saveProfileJsCode)
	pyperclip.copy(saveProfileJsCode)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")

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