from playwright.sync_api import sync_playwright, Request, Response


def log_request(request: Request):
    print(f"Request: {request.url}")


def log_response(response: Response):
    print(f"Response: {response.url} -> {response.status}")


def log_specific_requests(request: Request):
    if "googleapis.com" in request.url:
        print(f"Filtered request: {request.url}")


def log_response_body(response: Response):
    if response.ok:
        print(f"Response body: {response.body()}")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.on("request", log_specific_requests)
    page.on("response", log_response)

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.wait_for_timeout(3000)
