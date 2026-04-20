from time import time

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
            # //android.widget.TextView[@content-desc="API Demos"]
            # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="API Demos"]').click()
            # time.sleep(3)  # 요소 간의 간격을 위해 잠시 대기
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Preference"]').click()
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="3. Preference dependencies"]').click()
            self.driver.find_element(by=AppiumBy.ID, value='android:id/checkbox').click()
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ListView[@resource-id="android:id/list"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout').click()
            self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').send_keys("Hello")
            buttons = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.Button')
            buttons[1].click()

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