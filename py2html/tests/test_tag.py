from py2html import html


def test_tag():
    assert "<example></example>" == html.Tag("example").export()


def test_self_closing_tag():
    assert "<example>" == html.Tag("example", self_closing_tag=True).export()


def test_tag_inner():
    assert "<example>inner text</example>" == html.Tag("example", "inner text").export()


def test_tag_attrs():
    assert '<example a="1" b="2"></example>' == html.Tag("example", a="1", b="2").export()


def test_self_closing_tag_attrs():
    assert (
        '<example a="1" b="2">'
        == html.Tag("example", self_closing_tag=True, a="1", b="2").export()
    )
