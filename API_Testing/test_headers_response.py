from playwright.sync_api import Playwright


def test_headers_response(playwright: Playwright):

    request_context = playwright.request.new_context()
    response = request_context.get("https://www.google.com/")

    assert response.status_text == "OK"
    assert response.status == 200

    headers = response.headers

    for key,value in headers.items():
        print(f"{key}: {value}")

    # Check for specific headers


    print("Content-Type:", headers.get("content-type")) 
    assert "text/html" in headers.get("content-type")

    assert "gzip" in headers.get("content-encoding")


    # validate specific header present or not

    assert "server" in headers
    assert "set-cookie" in headers
