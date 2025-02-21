from py2html import html

import pytest


@pytest.fixture
def html_example():
    return """<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>"""


def test_doctype() -> None:
    assert "<!DOCTYPE html>" == html.Doctype().render()


def test_html() -> None:
    expected = "<html></html>"

    assert expected == html.Html().render()


def test_title() -> None:
    expected = "<title>Page Title</title>"

    assert expected == html.Title("Page Title").render()


def test_title_inside_head() -> None:
    expected = "<head><title>Page Title</title></head>"
    tag = html.Head()
    tag.add_child(html.Title("Page Title"))

    assert expected == tag.render()
