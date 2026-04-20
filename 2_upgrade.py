from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time


# AppiumConnection 클래스가 정의된 파일을 가져오기
from base import AppiumConnection  # base.py가 기본 파일명입니다.

class scrollingdemo(AppiumConnection):
    def examTest(self):
        try:
            print(f"요소를 기다리는 중...")
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="API Demos"]').click()
            time.sleep(3)
            
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Views"]').click()
            # time.sleep(3)
            # 예제 1 ------------------------------------------
            # start element
            # start_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Animation"]')
            # target element
            # target_el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Grid"]')
                        
            # scroll 실행
            try:
                # 예제 1 ------------------------------------------
                # self.driver.scroll(target_el, start_el)
                # 예제 2 ------------------------------------------
                # 실행 예제
                # scroll_until_element_visible(self.driver, '//android.widget.TextView[@text="WebView"]')

                # # 예제 3 ------------------------------------------
                # 특정 요소가 화면에 보일 때까지 스크롤 수행
                target_element = self.driver.find_element(
                    by=AppiumBy.ANDROID_UIAUTOMATOR, 
                    value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("WebView"))'
                )
                print("WebView 요소를 찾았습니다!")
                

            except Exception as e:
                print(f"Scroll Error: {e}")
            
            print(f"요소 테스트 완료!")
        except TimeoutException:
            print(f"요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")

# 예제 2 ------------------------------------------
# 특정 요소가 화면에 보일 때까지 스크롤 수행 함수
def scroll_until_element_visible(driver, target_xpath):
    while True:
        try:
            # 목표 요소 찾기
            target_element = driver.find_element(by=AppiumBy.XPATH, value=target_xpath)
            print("요소를 찾았습니다!")
            return target_element  # 요소 반환
        except NoSuchElementException:
            # 요소가 보이지 않을 경우 스크롤 수행
            print("요소를 찾을 수 없습니다. 스크롤 실행 중...")
            driver.execute_script("mobile: scrollGesture", {
                "left": 100,   # 스크롤 시작 영역의 X 좌표
                "top": 100,    # 스크롤 시작 영역의 Y 좌표
                "width": 800,  # 스크롤 영역의 너비
                "height": 1200, # 스크롤 영역의 높이
                "direction": "down",  # 스크롤 방향
                "percent": 0.75       # 한 번에 이동하는 화면 크기의 비율
            })



if __name__ == "__main__":
    automation = scrollingdemo()
    automation.connect()

    # 특정 앱에서 클릭 작업 수행
    if automation.driver:
        # 예: "com.example:id/button_start" 리소스 ID를 가진 버튼 클릭
        automation.examTest()
    
    automation.quit()