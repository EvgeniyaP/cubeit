from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"


def test_cube(page: Page):
    page.goto(BASE_URL)
    num_input = page.get_by_placeholder("enter number...")
    num_input.fill("5")

    button = page.get_by_role("button", name="Cube")
    button.click()

    result = page.locator("p#result")
    expect(result).to_contain_text("125")


def test_empty_input(page: Page):
    page.goto(BASE_URL)
    num_input = page.get_by_placeholder("enter number...")
    num_input.fill("")

    button = page.get_by_role("button", name="Cube")
    button.click()

    result = page.locator("p#result")
    expect(result).to_contain_text("Enter something!")
