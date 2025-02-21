from py2html import html

import pytest


@pytest.fixture
def html_example():
    return """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>
        
        </body>
        </html> 
    """


def test_doctype():
    assert "<!DOCTYPE html>" == html.Doctype().render()
