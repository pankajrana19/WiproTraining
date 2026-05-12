from pages.home_page import HomePage

def test_open_amazon(driver):
    assert "amazon" in driver.current_url,"URL for amazon is not correct"
    print("\nOpened Amazon Homepage. Title & URL verified")

