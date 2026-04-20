from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# AppiumConnection 클래스가 정의된 파일을 가져오기
from base import AppiumConnection  # base.py가 기본 파일명입니다.

class Uiautomatortest(AppiumConnection):
    def examTest(self):
        try:
            print(f"요소를 기다리는 중...")
            self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="API Demos"]').click()
            
            self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='text(\"Views\")').click()

            # 클릭 가능한 요소가 몇 개 있는지 확인
            clickable_elements = self.driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().clickable(true)')
            print(f"클릭 가능한 요소 수: {len(clickable_elements)}")
            
            print(f"요소 테스트 완료!")
        except TimeoutException:
            print(f"요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")

if __name__ == "__main__":
    automation = Uiautomatortest()
    automation.connect()

    # 특정 앱에서 클릭 작업 수행
    if automation.driver:
        # 예: "com.example:id/button_start" 리소스 ID를 가진 버튼 클릭
        automation.examTest()
    
    automation.quit()