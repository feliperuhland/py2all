from py2html import Tag


def test_tag():
    assert "<example></example>" == Tag("example").export()


def test_self_closing_tag():
    assert "<example>" == Tag("example", self_closing_tag=True).export()


def test_tag_inner():
    assert "<example>inner text</example>" == Tag("example", "inner text").export()


def test_tag_attrs():
    assert '<example a="1" b="2"></example>' == Tag("example", a="1", b="2").export()


def test_self_closing_tag_attrs():
    assert '<example a="1" b="2">' == Tag("example", self_closing_tag=True, a="1", b="2").export()
