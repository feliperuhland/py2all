from py2html import tag

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
    assert "<!DOCTYPE html>" == tag.Doctype().render()


def test_html() -> None:
    expected = "<html></html>"

    assert expected == tag.Html().render()


def test_title() -> None:
    expected = "<title>Page Title</title>"

    assert expected == tag.Title("Page Title").render()


def test_title_inside_head() -> None:
    expected = "<head><title>Page Title</title></head>"
    head = tag.Head()
    head.add_child(tag.Title("Page Title"))

    assert expected == head.render()


def test_document(html_example):
    doc = tag.Document(
        children=[
            tag.Doctype(),
            tag.Html(
                children=[
                    tag.Head(children=[tag.Title(text="Page Title")]),
                    tag.Body(
                        children=[
                            tag.H1(text="This is a Heading"),
                            tag.P(text="This is a paragraph."),
                        ]
                    ),
                ]
            ),
        ]
    )
    assert html_example.replace("\n", "") == doc.render()
