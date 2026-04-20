from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Appium 옵션 설정
options = UiAutomator2Options()
options.load_capabilities({
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14",
    "appium:settings[enableMultiWindows]": True,
    "appium:wdaLocalPort": "8100",
    "appium:settings[allowInvisibleElements]": True,
    "appium:connectHardwareKeyboard": True
})

# Appium 서버 연결
print("Appium 서버 연결 시도 중...")
try:
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    print("Appium 서버 연결 성공!")
except Exception as e:
    print(f"Appium 서버 연결 실패: {e}")
    exit(1)

# 요소 대기 및 클릭
try:
    element_id = '//android.widget.TextView[@content-desc="YouTube"]'  # 실제 앱의 요소 xpath로 변경
    print(f"요소 '{element_id}' 대기 중...")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element_id))
    )
    print("요소를 찾았습니다! 클릭 시도 중...")
    element.click()
    print("클릭 성공!")
except TimeoutException:
    print("요소를 찾는 데 시간이 초과되었습니다.")
except Exception as e:
    print(f"클릭 중 오류 발생: {e}")

# 드라이버 종료
print("테스트 종료, 드라이버 종료 중...")
driver.quit()
print("드라이버가 종료되었습니다.")