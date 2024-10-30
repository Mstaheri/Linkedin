# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# @given('the user is on the login page')
# def step_user_on_login_page(context):
#     context.browser.get('https://example.com/login')

# @when('the user enters valid username and password')
# def step_user_enters_valid_credentials(context):
#     username_input = context.browser.find_element(By.NAME, 'username')
#     password_input = context.browser.find_element(By.NAME, 'password')
#     login_button = context.browser.find_element(By.NAME, 'login')

#     username_input.send_keys('valid_username')
#     password_input.send_keys('valid_password')
#     login_button.click()

# @when('the user enters invalid username and password')
# def step_user_enters_invalid_credentials(context):
#     username_input = context.browser.find_element(By.NAME, 'username')
#     password_input = context.browser.find_element(By.NAME, 'password')
#     login_button = context.browser.find_element(By.NAME, 'login')

#     username_input.send_keys('invalid_username')
#     password_input.send_keys('invalid_password')
#     login_button.click()

# @then('the user should be redirected to the dashboard')
# def step_user_redirected_to_dashboard(context):
#     assert context.browser.current_url == 'https://example.com/dashboard'

# @then('an error message should be displayed')
# def step_error_message_displayed(context):
#     error_message = context.browser.find_element(By.CLASS_NAME, 'error').text
#     assert "Invalid credentials" in error_message