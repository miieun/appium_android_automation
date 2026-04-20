import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# AppiumConnection 클래스가 정의된 파일을 가져오기
from base import AppiumConnection  # base.py가 기본 파일명입니다.

class AppAutomation(AppiumConnection):
    def examTest(self):
        try:
            print(f"요소를 기다리는 중...")
            # 1. 유투브 실행
            # //android.widget.TextView[@content-desc="YouTube"]
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="YouTube"]').click()

            # 2. "검색" 버튼 있는 경우 클릭
            # //android.widget.ImageView[@content-desc="Search"]
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Search"]'))
            ).click()

            # 2. 검색에 "RPA test" 입력
            # //android.view.ViewGroup[@content-desc="Search YouTube"]
            # //android.widget.LinearLayout[@resource-id="com.google.android.youtube:id/search_box"]
            # //android.widget.EditText[@resource-id="com.google.android.youtube:id/search_edit_text"]            
            time.sleep(5)
            # self.driver.find_element(by=AppiumBy.CLASS_NAME, value='//android.widget.LinearLayout[@resource-id="com.google.android.youtube:id/search_box"]').send_keys("RPA test")
            # self.driver.switch_to.active_element.send_keys("RPA test")
            self.driver.press_keycode(46)  # R
            self.driver.press_keycode(44)  # P
            self.driver.press_keycode(29)  # A
            self.driver.press_keycode(62)  # SPACE
            self.driver.press_keycode(48)  # T
            self.driver.press_keycode(33)  # E
            self.driver.press_keycode(47)  # S
            self.driver.press_keycode(48)  # T


            # 3. 검색 버튼 클릭(엔터)
            # press_keycode(66)
            self.driver.press_keycode(66)
            # 4. 검색 결과 중 "RPA vs. Test Automation" 클릭
            # //android.widget.ImageButton[@content-desc="Navigate up"]
            time.sleep(5)
            # self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="RPA vs. Test Automation (3 key differences!) - 3 minutes, 47 seconds - Go to channel - What is RPA - 295 views - 2 years ago - play video"]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView').click()
            element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Navigate up"]')
            rect = element.rect  # 요소의 위치와 크기 정보 가져오기

            # 요소 중심 좌표 계산
            center_x = rect['x'] + rect['width'] / 2
            center_y = rect['y'] + rect['height'] / 2

            # 오프셋 적용
            adjusted_x = center_x + 200
            adjusted_y = center_y + 300

            # Appium의 'clickGesture' 사용
            self.driver.execute_script('mobile: clickGesture', {
                'x': center_x,
                'y': adjusted_y
            })
            
            # 5. 5초 후 "skip" 클릭
            # time.sleep(5)
            # //android.widget.TextView[@resource-id="com.google.android.youtube:id/skip_ad_button_text"]
            # WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.google.android.youtube:id/skip_ad_button_text"]'))
            # ).click()
            elements = self.driver.find_elements(
                by=AppiumBy.XPATH,
                value='//android.widget.TextView[@resource-id="com.google.android.youtube:id/skip_ad_button_text"]'
            )

            if elements:
                elements[0].click()
                print("광고 스킵 버튼 클릭 완료")
            else:
                print("홈 버튼 클릭")
                # 6. 유투브 아이콘이 보일 때까지 백 버튼 클릭
                # self.driver.press_keycode(4)
                # or 홈 버튼 클릭
                # press_keycode(3)  # KEYCODE_HOME
                self.driver.press_keycode(3)           

            # 7. Gmail 아이콘 롱 클릭
            # //android.widget.TextView[@content-desc="Gmail"]
            # 대상 요소의 좌표 가져오기
            time.sleep(5)
            element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Gmail"]')
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
            
            # 8. "App Info" 클릭
            # //android.widget.TextView[@resource-id="com.google.android.apps.nexuslauncher:id/bubble_text" and @text="App info"]
            time.sleep(5)
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.apps.nexuslauncher:id/bubble_text" and @text="App info"]').click()
            
            # 9. "back" 버튼 클릭
            self.driver.press_keycode(4)

            print(f"요소 테스트 완료!")
        except TimeoutException:
            print(f"요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")

if __name__ == "__main__":
    automation = AppAutomation()
    automation.connect()

    # 특정 앱에서 클릭 작업 수행
    if automation.driver:
        # 예: "com.example:id/button_start" 리소스 ID를 가진 버튼 클릭
        automation.examTest()
    
    automation.quit()