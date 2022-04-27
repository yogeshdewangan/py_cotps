import random
import time, logging

log = logging.getLogger(__name__)

import getconfig
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

portal = getconfig.props["portal"]
phone_number = getconfig.props["phone_number"]
password = getconfig.props["password"]
wait_for_next_cycle_hour = int(getconfig.props["wait_for_next_cycle_hour"])

log.info("portal: " + portal)
log.info("phone_number: " + str(phone_number))
log.info("password: " + password)
log.info("wait_for_next_cycle_hour: " + str(wait_for_next_cycle_hour) + " hour")


def start():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    log.info("Browser opened")
    driver.maximize_window()
    log.info("Browser maximized")

    driver.get(portal)
    log.info("Navigated to : " + portal)
    time.sleep(2)

    # login(driver, phone_number, password)
    total_transactions = 0
    for i in range(0, 500):
        log.info("Loop count: " + str(i))

        try:

            if "Log in" in driver.title:
                login(driver, phone_number, password)


            driver.find_elements(by=By.CLASS_NAME, value="uni-tabbar__label")[1].click()
            log.info("Transaction hall button clicked")
            time.sleep(2)
            wallet_balance = float(
                driver.find_element(by=By.CLASS_NAME, value="division-right").find_element(by=By.CLASS_NAME,
                                                                                           value="division-num").text)
            log.info("Wallet balance: " +str(wallet_balance))

            if wallet_balance > 5:
                log.info("Wallet balance is more than 5. So it will continue buying crypto")
                driver.find_element(by=By.CLASS_NAME, value="orderBtn").click()
                log.info("Order button clicked")
                time.sleep(7)

                xpath_sell_button = "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]"
                driver.find_element(by=By.XPATH, value=xpath_sell_button).click()
                log.info("Sell button clicked")
                time.sleep(7)
                try:
                    xpath_confirm_button = "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button"
                    driver.find_element(by=By.XPATH, value=xpath_confirm_button).click()
                    log.info("Confirm button clicked")
                    time.sleep(6)
                except Exception as e:
                    log.info(str(e))


                total_transactions +=1
                log.info("Total transactions : " + str(total_transactions))

                driver.refresh()

            else:
                sleep_time = 900
                log.info("Waiting for : " + str(sleep_time) + " seconds")
                
                time.sleep(sleep_time)
                
                driver.refresh()
                continue


            time.sleep(10)


        except Exception as e:
            log.info(str(e))


def login(driver, phone_number, password):
    xpath_country_code = "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-text"

    driver.find_element(by=By.XPATH, value=xpath_country_code).click()
    time.sleep(1)

    driver.find_element(by=By.CLASS_NAME, value="uni-input-input").send_keys("91")
    time.sleep(1)

    xpath_confirm_button = "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-button"

    driver.find_element(by=By.XPATH, value=xpath_confirm_button).click()
    time.sleep(2)

    input_elements = driver.find_elements(by=By.CLASS_NAME, value="uni-input-input")
    input_elements[0].send_keys(phone_number)
    time.sleep(1)
    input_elements[1].send_keys(password)
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME, value="login").click()
    time.sleep(5)
    log.info("Login succeeded")


if __name__ == '__main__':
    start()
