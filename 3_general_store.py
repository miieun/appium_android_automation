from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

from base import AppiumConnection

class GeneralStoreTest(AppiumConnection):
    def examTest(self):
        try:
            print("요소를 기다리는 중...")
            time.sleep(2)
            # 현재 화면 확인
            # print("현재 패키지:", self.driver.current_package)
            # print("현재 Activity:", self.driver.current_activity)
            # print("현재 화면 XML:")
            # print(self.driver.page_source[:2000])  # 추가

           # 2. 국가 "Angola" 선택
            self.driver.find_element(
                AppiumBy.ID, "com.androidsample.generalstore:id/spinnerCountry").click()
            time.sleep(1)
            self.driver.find_element(
                AppiumBy.XPATH, '//android.widget.TextView[@text="Angola"]').click()
            print("Angola 선택")

            # 3. "Your Name" 빈칸으로 둠 (아무것도 안 함)
            print("Your Name 빈칸 유지")

            # 4. "Female" 선택
            self.driver.find_element(
                AppiumBy.ID, "com.androidsample.generalstore:id/radioFemale").click()
            print("Female 선택")

            # 5. "Let's Shop" 버튼 클릭
            self.driver.find_element(
                AppiumBy.ID, "com.androidsample.generalstore:id/btnLetsShop").click()
            print("Let's Shop 클릭")
            time.sleep(2)

            # 6. 토스트 확인 후 현재 화면 체크
            current_activity = self.driver.current_activity
            print(f"현재 Activity: {current_activity}")

            # 아직 MainActivity면 토스트 뜨고 그대로인 것
            if "MainActivity" in current_activity:
                print("토스트 메시지로 인해 화면 유지")

            # 7. "Your Name"에 "kim" 입력
            name_field = self.driver.find_element(
                AppiumBy.ID, "com.androidsample.generalstore:id/nameField")
            name_field.clear()
            name_field.send_keys("kim")
            print("이름 kim 입력")

             # 키보드 숨기기
            self.driver.hide_keyboard()
            time.sleep(1)

            # 다시 Let's Shop 클릭
            self.driver.find_element(
                AppiumBy.ID, "com.androidsample.generalstore:id/btnLetsShop").click()
            time.sleep(2)

            # 8. 스크롤해서 "Air Jordan 9 Retro" 장바구니 담기
            found = False

            for _ in range(10):
                products = self.driver.find_elements(
                    AppiumBy.ID,
                    "com.androidsample.generalstore:id/productName"
                )

                add_buttons = self.driver.find_elements(
                    AppiumBy.ID,
                    "com.androidsample.generalstore:id/productAddCart"
                )

                for i in range(len(products)):
                    product_name = products[i].text

                    if product_name == "Air Jordan 9 Retro":
                        print("Air Jordan 9 Retro 발견")

                        button_text = add_buttons[i].text
                        print(f"버튼 상태: {button_text}")

                        if button_text == "ADD TO CART":
                            add_buttons[i].click()
                            print("장바구니 담기 완료")
                        else:
                            print("이미 장바구니에 있음")

                        found = True
                        break

                if found:
                    break

                print("상품 없음 → 스크롤")
                self.driver.execute_script('mobile: scrollGesture', {
                    'left': 100, 'top': 300,
                    'width': 900, 'height': 1500,
                    'direction': 'down',
                    'percent': 0.5
                })
                time.sleep(1)

            if not found:
                print("Air Jordan 9 Retro 못 찾음")

            # 9. 장바구니 클릭
            self.driver.find_element(
                AppiumBy.ID,
                "com.androidsample.generalstore:id/appbar_btn_cart"
            ).click()

            print("장바구니 클릭")
            time.sleep(2)

            # 10. Air Jordan 9 Retro 상품 있는지 확인
            try:
                item = self.driver.find_element(
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Air Jordan 9 Retro"]')
                print(f"✓ 장바구니에 상품 확인: {item.text}")
            except NoSuchElementException:
                print("장바구니에 상품 없음")

            # 11. "Please read our terms of conditions" 롱 클릭
            terms = self.driver.find_element(
                AppiumBy.ID,
                "com.androidsample.generalstore:id/termsButton")
            rect = terms.rect
            center_x = rect['x'] + rect['width'] / 2
            center_y = rect['y'] + rect['height'] / 2

            self.driver.execute_script('mobile: longClickGesture', {
                'x': center_x,
                'y': center_y,
                'duration': 2000
            })
            print("Terms 롱 클릭")
            time.sleep(1)

            # 12. "Terms Of Conditions" 확인 후 CLOSE 클릭
            try:
                title = self.driver.find_element(
                    AppiumBy.XPATH,
                    '//*[contains(@text,"Terms Of Conditions") or contains(@text,"Terms of Conditions")]')
                print(f"팝업 확인: {title.text}")
            except NoSuchElementException:
                print("팝업 타이틀 못찾음")

            self.driver.find_element(
                AppiumBy.XPATH,
                '//*[contains(@text,"CLOSE") or contains(@text,"Close")]').click()
            print("CLOSE 클릭")
            time.sleep(1)

            # 13. 체크박스 클릭
            checkbox = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.CheckBox[contains(@text,"e-mails")]'
                ))
            )
            checkbox.click()
            print("체크박스 클릭")

            # 14. "Visit to the website to completes purchase" 버튼 클릭
            self.driver.find_element(
                AppiumBy.ID,
                "com.androidsample.generalstore:id/btnProceed").click()
            print("구매 버튼 클릭")
            time.sleep(3)

            # 15. 브라우저로 이동 확인
            current_pkg = self.driver.current_package
            print(f"현재 앱 패키지: {current_pkg}")
            if "chrome" in current_pkg or "browser" in current_pkg:
                print("브라우저로 이동 확인")
            else:
                print(f"현재 화면: {current_pkg}")

            # 16. 백 버튼 클릭
            self.driver.press_keycode(4)
            print("백 버튼 클릭")
            time.sleep(2)

            # 17. 첫 화면으로 이동 확인
            current_activity = self.driver.current_activity
            print(f"현재 Activity: {current_activity}")

            # 18. 백 버튼 두 번 클릭해 종료
            self.driver.press_keycode(4)
            time.sleep(1)
            self.driver.press_keycode(4)
            print("백 버튼 2회 클릭 종료")

            print("\n테스트 완료!")

        except TimeoutException:
            print("요소를 찾는 데 시간이 초과되었습니다.")
        except Exception as e:
            print(f"요소 테스트 중 오류 발생: {e}")

if __name__ == "__main__":
    automation = GeneralStoreTest()
    automation.connect()
    if automation.driver:
        automation.examTest()
    automation.quit()