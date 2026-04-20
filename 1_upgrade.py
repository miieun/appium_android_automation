from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
import time


# AppiumConnection 클래스가 정의된 파일을 가져오기
from base import AppiumConnection  # base.py가 기본 파일명입니다.

class swipedemo(AppiumConnection):
    def examTest(self):
        try:
            print(f"요소를 기다리는 중...")
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="API Demos"]').click()
            time.sleep(3)
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Views"]').click()
            time.sleep(3)
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Date Widgets"]').click()

            self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='text(\"2. Inline\")').click()
            # hour
            self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="9"]').click()

            # minute
            # first element
            first_el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="15"]')
            # second element
            second_el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="45"]')
            
            # 첫 번째 요소의 위치와 크기
            first_rect = first_el.rect
            first_x = first_rect['x'] + first_rect['width'] / 2
            first_y = first_rect['y'] + first_rect['height'] / 2            

            # 두 번째 요소의 위치와 크기
            second_rect = second_el.rect
            second_x = second_rect['x'] + second_rect['width'] / 2
            second_y = second_rect['y'] + second_rect['height'] / 2

            # 첫 번째 요소의 위치 확인
            print(f"First Element Rect: {first_rect}")
            print(f"First Element Center: ({first_x}, {first_y})")

            # 두 번째 요소의 위치 확인
            print(f"Second Element Rect: {second_rect}")
            print(f"Second Element Center: ({second_x}, {second_y})")

            # swipeGesture 실행
            try:
                self.driver.swipe(first_x, first_y, second_x, second_y, 1000)

            except Exception as e:
                print(f"Swipe Gesture Error: {e}")
            
            print(f"요소 테스트 완료!")
        except TimeoutException:
            print(f"요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")

if __name__ == "__main__":
    automation = swipedemo()
    automation.connect()

    # 특정 앱에서 클릭 작업 수행
    if automation.driver:
        # 예: "com.example:id/button_start" 리소스 ID를 가진 버튼 클릭
        automation.examTest()
    
    automation.quit()