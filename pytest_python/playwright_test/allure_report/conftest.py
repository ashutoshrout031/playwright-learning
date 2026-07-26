from pathlib import Path
import pytest
import allure
from slugify import slugify 


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to modify the test report and add a slugified test name to the report.
    This can be useful for generating unique identifiers for test cases.
    """

    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=screen_file)

        if (report.skipped and xfail) or (report.failed and not xfail):
            # add an image to the html report
            extra.append(pytest_html.extras.png(screen_file))

            allure.attach.file(
                screen_file, 
                name="Failure_Screenshot", 
                attachment_type=allure.attachment_type.PNG
                )
        report.extra = extra
            
    