from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user.name@gmail.com")

    # email_input = page.locator('[data-testid="registration-form-email-input"] input')
    # email_input = page.get_by_test_id("registration-form-email-input").get_by_role("textbox")

    # Заполняем поле username
    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill("username")

    # Заполняем поле пароль
    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # # Проверяем, что появилось сообщение об ошибке
    # wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # expect(wrong_email_or_password_alert).to_be_visible()
    # expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)
