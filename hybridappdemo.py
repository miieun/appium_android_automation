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
            print(f"디바이스 완전 초기화 중...")
            self.terminate_current_app(self.driver)
            print(f"디바이스 완전 초기화 완료!")

            print(f"요소를 기다리는 중...")
            # 앱 재시작
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="GeneralStore"]').click()
            time.sleep(5)
            self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').send_keys("Hello")
            # go to shop
            self.driver.find_element(by=AppiumBy.ID, value='com.androidsample.generalstore:id/btnLetsShop').click()
            time.sleep(2)
            
            # add to cart
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="ADD TO CART"]').click()
            # go to cart
            self.driver.find_element(by=AppiumBy.ID, value='com.androidsample.generalstore:id/appbar_btn_cart').click()
            time.sleep(2)
            
            # check the checkbox
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.CheckBox[@text="Send me e-mails on discounts related to selected products in future"]').click()

            # find the terms and conditions
            element = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Please read our terms of conditions"]')
            rect = element.rect  # 요소의 위치와 크기 정보 가져오기

            # 요소 중심 좌표 계산
            center_x = rect['x'] + rect['width'] / 2
            center_y = rect['y'] + rect['height'] / 2

            # Appium의 'longClickGesture' 사용
            self.driver.execute_script('mobile: longClickGesture', {
                'x': center_x,
                'y': center_y,
                'duration': 2000  # LongPress 지속 시간 (밀리초, 예: 2000ms = 2초)
            })

            # click on close
            self.driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()

            # click on visit website
            self.driver.find_element(by=AppiumBy.ID, value='com.androidsample.generalstore:id/btnProceed').click()            
            time.sleep(3)

            # type codenbox in google search
            context_names = self.driver.contexts  # both context names

            for context_name in context_names:
                print(context_name)  # prints out something like NATIVE_APP \n WEBVIEW_1


            # 웹뷰 컨텍스트로 전환
            self.driver.switch_to.context("WEBVIEW_com.androidsample.generalstore")

            # 2초 대기
            time.sleep(2)

            # 입력 필드에 "codenbox" 입력 후 Enter 키 입력
            search_box = self.driver.find_element(By.NAME, "q")
            # search_box.send_keys("codenbox")
            # search_box.send_keys(Keys.ENTER)           
            
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