from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def main():
  driver = webdriver.Firefox()
  driver.get("https://steamcommunity.com")
  driver.maximize_window()

  loginXpath = "/html/body/div[1]/div[7]/div[1]/div/div[3]/div/a[2]"

  if check_exists_by_xpath(driver, loginXpath):
    print("You are not logged in to Steam. Cannot edit Display Name")
  else:
    print("User is Logged in")

  driver.quit()

def check_exists_by_xpath(driver, xpath):
  try:
    driver.find_element(By.XPATH, xpath)
    return True
  except NoSuchElementException:
    return False

if __name__ == '__main__':
  main()