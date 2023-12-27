from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import keyboard
import time

def main():
  newName = "Test"

  keyboard.send("win")
  time.sleep(0.2)
  keyboard.write("Firefox") # Update this line for a different browser
  time.sleep(0.2)
  keyboard.press_and_release("enter")
  time.sleep(3) # Wait for page to load

  keyboard.send("alt+d")
  keyboard.write("https://steamcommunity.com")
  keyboard.press_and_release("enter")
  time.sleep(3) # Wait for page to load

  LoopTabbing(timesToLoop=2)
  keyboard.press_and_release("enter")
  time.sleep(1) # Wait for page to load

  LoopTabbing(timesToLoop=27)
  keyboard.press_and_release("enter")
  time.sleep(1) # Wait for page to load

  LoopTabbing(timesToLoop=40)
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