import os

def test_login_page(driver):
    file_path = os.path.abspath("app/index.html")
    driver.get("file://" + file_path)
    # driver.get("file:///Users/snehasishdey/Desktop/reg-form/app/index.html")

    assert "Login Page" in driver.page_source

    username = driver.find_element("id", "username")
    password = driver.find_element("id", "password")
    button   = driver.find_element("id", "loginBtn")

    username.send_keys("test")
    password.send_keys("123")
    button.click()

    assert True
