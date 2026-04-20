from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.appiumby import AppiumBy
import time


# AppiumConnection 클래스가 정의된 파일을 가져오기
from base import AppiumConnection  # base.py가 기본 파일명입니다.

class gestures(AppiumConnection):
    def examTest(self):
        try:
            print(f"요소를 기다리는 중...")
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="API Demos"]').click()
            time.sleep(3)

            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Views"]').click()
            time.sleep(3)

            # 대상 요소의 좌표 가져오기
            element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Expandable Lists"]')
            rect = element.rect  # 요소의 위치와 크기 정보 가져오기

            # 요소 중심 좌표 계산
            center_x = rect['x'] + rect['width'] / 2
            center_y = rect['y'] + rect['height'] / 2

            # Appium의 'clickGesture' 사용
            self.driver.execute_script('mobile: clickGesture', {
                'x': center_x,
                'y': center_y
            })
            time.sleep(3)

            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="1. Custom Adapter"]').click()
            time.sleep(3)

            # 대상 요소의 좌표 가져오기
            element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="People Names"]')
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

            el = self.driver.find_element(by=AppiumBy.ID, value='android:id/title')
            # 요소가 표시되는지 확인
            if el.is_displayed():
                print(f"요소가 표시되었습니다: {el.text}")
            else:
                print(f"요소가 표시되지 않았습니다.")                
            
            print(f"요소 테스트 완료!")
        except TimeoutException:
            print(f"요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")

if __name__ == "__main__":
    automation = gestures()
    automation.connect()

    # 특정 앱에서 클릭 작업 수행
    if automation.driver:
        # 예: "com.example:id/button_start" 리소스 ID를 가진 버튼 클릭
        automation.examTest()
    
    automation.quit()