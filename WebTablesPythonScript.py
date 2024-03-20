from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the path to your WebDriver executable
driver_path = '/Applications/chromedriver-mac-x64'

def main():
    driver = webdriver.Chrome(executable_path='/Applications/chromedriver-mac-x64')
    driver.get('http://www.way2automation.com/angularjs-protractor/webtables/')

    # Scenario 1: Add a user and validate
    add_user('Test', 'User', 'testuser', driver)

    # Scenario 2: Delete user "novak" and validate
    delete_user('novak', driver)

    driver.quit()

def add_user(first_name, last_name, username, driver):
    # Locate form input fields
    first_name_input = driver.find_element(By.ID, 'firstName')
    last_name_input = driver.find_element(By.ID, 'lastName')
    username_input = driver.find_element(By.ID, 'userName')
    add_button = driver.find_element(By.CSS_SELECTOR, '.add-btn')

    # Fill form fields with user information
    first_name_input.send_keys(first_name)
    last_name_input.send_keys(last_name)
    username_input.send_keys(username)

    # Click the add button
    add_button.click()

    # Wait for the table to update
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#table tbody tr:nth-child(last)')))
    except:
        print("Failed to find newly added user.")

    # Get the last row cells
    last_row_cells = driver.find_elements(By.CSS_SELECTOR, '#table tbody tr:last-child td')

    # Validate that the added user's details are present
    assert last_row_cells[0].text == first_name
    assert last_row_cells[1].text == last_name
    assert last_row_cells[2].text == username

def delete_user(username, driver):
    # Find the row containing the username
    user_row = driver.find_element(By.XPATH, f'//tr[td[text()="{username}"]]')
    delete_button = user_row.find_element(By.CSS_SELECTOR, '.delete-btn')
    delete_button.click()

    # Wait for the row to disappear
    try:
        WebDriverWait(driver, 5).until(
            EC.staleness_of(user_row))
    except:
        print(f"Failed to delete user '{username}'.")

if __name__ == '__main__':
    main()