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

class DragDropdemo(AppiumConnection):
    def examTest(self):
        try:
            print(f"요소를 기다리는 중...")
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="API Demos"]').click()
            time.sleep(3)            
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Views"]').click()

            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Drag and Drop"]').click()
            # time.sleep(3)
            
            try:                    
                # 첫 번째 요소 (드래그 시작 지점)
                # //android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_1"]
                # start_element = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.view.View')
                start_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_1"]')


                # 두 번째 요소 (드래그 종료 지점)
                # end_element = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.view.View')[1]  # 두 번째 인덱스 요소 선택

                # 첫 번째 요소의 중심 좌표 계산
                start_rect = start_element.rect
                start_x = start_rect['x'] + start_rect['width'] / 2
                start_y = start_rect['y'] + start_rect['height'] / 2
                print(f"start_x: {start_x} , start_y: {start_y}")

                # 두 번째 요소의 중심 좌표 계산
                # end_rect = end_element.rect
                # end_x = end_rect['x'] + end_rect['width'] / 2
                # end_y = end_rect['y'] + end_rect['height'] / 2
                end_x = start_x + 400
                end_y = start_y + 400
                print(f"end_x: {end_x} , end_y: {end_y}")

                # Drag and Drop 수행
                self.driver.execute_script('mobile: longClickGesture', {
                    'x': start_x,
                    'y': start_y,
                    'duration': 2000  # Long press 지속 시간 (밀리초 단위)
                })
                self.driver.execute_script('mobile: dragGesture', {
                    'startX': start_x,
                    'startY': start_y,
                    'endX': end_x,
                    'endY': end_y,
                    'duration': 2000  # 밀리초 단위로 드래그 지속시간 (예: 2초)
                })               

            except Exception as e:
                print(f"Drag and Drop Error: {e}")
            
            print(f"요소 테스트 완료!")
        except TimeoutException:
            print(f"요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")


if __name__ == "__main__":
    automation = DragDropdemo()
    automation.connect()

    # 특정 앱에서 클릭 작업 수행
    if automation.driver:
        # 예: "com.example:id/button_start" 리소스 ID를 가진 버튼 클릭
        automation.examTest()
    
    automation.quit()