import keyboard
import json
import pyperclip
import os
import time

BROWSER = "Firefox"
DELAY_BETWEEN_KEYS = 0.2
TIMEOUT_TO_LOAD_PAGE = 3

def main():
	OpenBrowser()
	OpenSteamWebpage()

	scriptDirectory = os.path.dirname(__file__)
	jsonDirectory = os.path.join(scriptDirectory, "JavaScriptCommands.json")
	with open(jsonDirectory) as json_file:
		jsonData = json.load(json_file)

	OpenProfile(jsonData)
	OpenEditProfile()
	EditProfileName()
	SaveProfileEdits(jsonData)

	keyboard.send("ctrl+w")

def OpenBrowser():
	keyboard.send("win")
	time.sleep(DELAY_BETWEEN_KEYS)
	keyboard.write(BROWSER)
	time.sleep(DELAY_BETWEEN_KEYS)
	keyboard.press_and_release("enter")
	time.sleep(TIMEOUT_TO_LOAD_PAGE)

def OpenSteamWebpage():
	steamURL = "https://steamcommunity.com"
	keyboard.send("alt+d")
	keyboard.write(steamURL)
	keyboard.press_and_release("enter")
	time.sleep(TIMEOUT_TO_LOAD_PAGE)

def OpenProfile(jsonData):
	keyboard.send("f12")
	time.sleep(DELAY_BETWEEN_KEYS)
	keyboard.send("ctrl+shift+k")
	time.sleep(DELAY_BETWEEN_KEYS)
	profileUrlJsCode = jsonData["GoToProfileURL"]
	profileUrlJsCode = "\n".join(profileUrlJsCode)
	pyperclip.copy(profileUrlJsCode)
	keyboard.send("ctrl+v")
	time.sleep(0.2)
	keyboard.press_and_release("enter")
	time.sleep(TIMEOUT_TO_LOAD_PAGE)

def OpenEditProfile():
	keyboard.send("f12")
	keyboard.send("alt+d")
	time.sleep(DELAY_BETWEEN_KEYS)
	keyboard.send("right arrow")
	time.sleep(DELAY_BETWEEN_KEYS)
	keyboard.write("edit/info")
	keyboard.press_and_release("enter")
	time.sleep(TIMEOUT_TO_LOAD_PAGE)

def EditProfileName():
	keyboard.send("f12")
	time.sleep(DELAY_BETWEEN_KEYS)
	keyboard.send("ctrl+shift+k")
	profileNameJavascript = GetProfileNameJavascript(NEW_DISPLAY_NAME)
	pyperclip.copy(profileNameJavascript)
	keyboard.send("ctrl+v")
	time.sleep(DELAY_BETWEEN_KEYS)
	keyboard.press_and_release("enter")
	time.sleep(DELAY_BETWEEN_KEYS)

def SaveProfileEdits(jsonData):
	saveProfileJsCode = jsonData["SaveChanges"]
	saveProfileJsCode = "\n".join(saveProfileJsCode)
	pyperclip.copy(saveProfileJsCode)
	keyboard.send("ctrl+v")
	time.sleep(DELAY_BETWEEN_KEYS)
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