from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch the Chromium browser in non-headless mode for visibility
    browser = playwright.chromium.launch(headless=False)
    # Create a new, isolated browser context (like an incognito session)
    context = browser.new_context()
    # Create a new page (tab) in the context
    page = context.new_page()

    # Navigate to a specific URL
    page.goto("https://playwright.dev/python/docs/intro")
    print(f"Page title: {page.title()}")

    # Click a link with specific text
    page.locator("text=Installation").click()
    
    # Assert that the new page title is correct (Playwright assertions auto-wait)
    assert "Installation | Playwright Python" in page.title()

    # Take a screenshot and save it
    page.screenshot(path="screenshot_example.png")

    # Close the browser
    browser.close()

# Run the automation within the Playwright context manager
with sync_playwright() as playwright:
    run(playwright)
