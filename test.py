from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time
import os


# AppiumConnection 클래스가 정의된 파일을 가져오기
from base import AppiumConnection  # base.py가 기본 파일명입니다.

class hybridappdemo(AppiumConnection):
    def examTest(self):
        try:
            

            print(f"요소를 기다리는 중...")
            self.driver.switch_to.context("WEBVIEW_com.androidsample.generalstore")
            time.sleep(2)
            

            # 입력 필드에 "codenbox" 입력 후 Enter 키 입력
            # //android.widget.EditText
            search_box = self.driver.find_element(By.NAME, "q")
            # search_box = self.driver.find_element(By.XPATH, '//android.widget.SearchView[@resource-id="tsf"]/android.view.View[1]')

            search_box.send_keys("codenbox")
            search_box.send_keys(Keys.ENTER)           
            
            print(f"요소 테스트 완료!")
        except TimeoutException:
            print(f"요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")

    def terminate_current_app(self, driver):
        try:
            # 현재 실행 중인 앱의 패키지명 확인
            current_app = driver.current_package
            print(f"현재 실행 중인 앱의 패키지명: {current_app}")
            
            # 앱 종료 수행
            if current_app:
                driver.terminate_app(current_app)
                print(f"{current_app} 앱을 종료했습니다.")
            else:
                print("현재 실행 중인 앱을 확인할 수 없습니다.")
        except Exception as e:
            print(f"앱 종료 중 오류 발생: {e}")


if __name__ == "__main__":
    automation = hybridappdemo()
    automation.connect()

    # 특정 앱에서 클릭 작업 수행
    if automation.driver:
        # 예: "com.example:id/button_start" 리소스 ID를 가진 버튼 클릭
        automation.examTest()
    
    automation.quit()