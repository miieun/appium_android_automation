from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
import time

from base import AppiumConnection

class YoutubeTest(AppiumConnection):
    def examTest(self):
        try:
            print("요소를 기다리는 중...")

            # 1. 유튜브 실행
            self.driver.execute_script('mobile: startActivity', {
                'intent': 'com.google.android.youtube/.app.honeycomb.Shell$HomeActivity'
            })
            time.sleep(3)

            # 2. 검색 버튼 클릭
            try:
                self.driver.find_element(
                    by=AppiumBy.ACCESSIBILITY_ID, value="Search").click()
                print("검색 버튼 클릭")
            except NoSuchElementException:
                print("검색 버튼 없음 → 2-1 진행")

            time.sleep(1)

            # 2-1. 검색창에 "RPA test" 입력
            try:
                self.driver.find_element(
                    by=AppiumBy.XPATH,
                    value='//android.widget.EditText').send_keys("RPA test")
                print("send_keys 입력 완료")
            except Exception:
                for key in [82, 47, 9, 60, 56, 62, 60, 56, 56, 60]:  # press_keycode 대체
                    self.driver.press_keycode(key)
                print("press_keycode 입력 완료")

            # 3. 엔터
            self.driver.press_keycode(66)
            print("엔터 클릭")
            time.sleep(2)

            # 4. 뒤로가기 아이콘 기준 X+200, Y+300 클릭
            back_btn = self.driver.find_element(
                by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
            target_x = back_btn.location['x'] + 200
            target_y = back_btn.location['y'] + 300
            print(f"클릭 좌표: ({target_x}, {target_y})")

            self.driver.execute_script('mobile: clickGesture', {
                'x': target_x,
                'y': target_y
            })
            print("첫 번째 영상 클릭")
            time.sleep(5)

            # 5. skip 버튼 확인 후 클릭, 없으면 홈 버튼
            try:
                skip_btn = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((
                        AppiumBy.XPATH,
                        '//*[contains(@text,"Skip") or contains(@text,"skip")]'
                    ))
                )
                skip_btn.click()
                print("Skip 클릭")
            except TimeoutException:
                self.driver.press_keycode(3)
                print("Skip 없음 → 홈 버튼 클릭")
            time.sleep(2)

            # 6. Gmail 롱 클릭
            gmail = self.driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Gmail"]')
            
            center_x = gmail.rect['x'] + gmail.rect['width'] / 2
            center_y = gmail.rect['y'] + gmail.rect['height'] / 2

            self.driver.execute_script('mobile: longClickGesture', {
                'x': center_x,
                'y': center_y,
                'duration': 2000
            })
            print("Gmail 롱 클릭")
            time.sleep(1)

            # 7. App Info 클릭
            self.driver.find_element(
                by=AppiumBy.XPATH,
                value='//*[contains(@text,"App info") or contains(@text,"App Info")]'
            ).click()
            print("App Info 클릭")
            time.sleep(1)

            # 8. 뒤로 가기
            self.driver.press_keycode(4)
            print("Back 클릭")

            print(f"요소 테스트 완료!")

        except TimeoutException:
            print(f"요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")

if __name__ == "__main__":
    automation = YoutubeTest()
    automation.connect()
    if automation.driver:
        automation.examTest()
    automation.quit()