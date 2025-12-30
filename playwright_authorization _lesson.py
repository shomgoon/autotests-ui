from playwright.sync_api import sync_playwright, expect

def test_elements_presence():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 1. Открыть страницу
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        
        # 2. Проверить наличие поля Email
        email_field = page.get_by_test_id("login-form-email-input")
        expect(email_field).to_be_visible()
        print("✅ Поле Email найдено")
        
        # 3. Проверить наличие поля Password
        password_field = page.get_by_test_id("login-form-password-input")
        expect(password_field).to_be_visible()
        print("✅ Поле Password найдено")
        
        # 4. Проверить наличие кнопки Login
        login_button = page.get_by_test_id("login-page-login-button")
        expect(login_button).to_be_visible()
        print("✅ Кнопка Login найдена")
        
        # 5. Проверить текст на кнопке
        expect(login_button).to_have_text("Login")
        print("✅ Кнопка имеет текст 'Login'")
        
        # Дополнительно: проверить placeholder полей
        email_input = email_field.locator("input")
        password_input = password_field.locator("input")
        
        # Можем проверить атрибуты
        expect(email_input).to_have_attribute("type", "email")
        expect(password_input).to_have_attribute("type", "password")
        
        print("✅ Все элементы присутствуют на странице")
        browser.close()

if __name__ == "__main__":
    test_elements_presence()