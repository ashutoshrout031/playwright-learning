from playwright.sync_api import Playwright


def test_headers_response(playwright: Playwright):

    request_context = playwright.request.new_context()
    response = request_context.get("https://www.google.com/")

    assert response.status_text == "OK"
    assert response.status == 200

    # We can only extract cookies from request context. cookies only stored in request context

    cookies = request_context.storage_state()["cookies"]

    print(cookies)

    for c in cookies:
        print(f"{c['name']} ====>{c['value']}, {c['domain']}")

    # Check if 'AEC' cookie is present in the response cookies

    aec_cookie = None

    for c in cookies:
        if c['name'] == 'AEC':
            aec_cookie = c

    assert aec_cookie is not None, "Cookie 'AEC' is not found"

    # printing details of 'AEC' cookie

    



