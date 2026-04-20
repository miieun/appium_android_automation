from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# AppiumConnection 클래스가 정의된 파일을 가져오기
from browser_base import AppiumConnection  # webview_base.py가 기본 파일명입니다.

class Test(AppiumConnection):
    def examTest(self):
        try:
            print(f"디바이스 완전 초기화 중...")
            # self.terminate_current_app(self.driver)
            print(f"디바이스 완전 초기화 완료!")

            
            self.driver.get("https://rahulshettyacademy.com/angularAppdemo/")
            
 
            print("요소 테스트 완료!")

        except TimeoutException:
            print("오류: 요소를 찾는 데 시간이 초과되었습니다.")
        except AssertionError as e:
            print(f"Assertion Error 발생: {e}")  # AssertionError 세부 메시지 출력
        except Exception as e:
            print(f"알 수 없는 오류 발생: {e}")

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
    automation = Test()
    automation.connect()

    # 특정 앱에서 클릭 작업 수행
    if automation.driver:
        # 예: "com.example:id/button_start" 리소스 ID를 가진 버튼 클릭
        automation.examTest()
    
    automation.quit()