from typing import TypeVar, Optional


Self = TypeVar("Self", bound="TagModel")


class TagModel:
    tag_name = ""
    self_closing = False

    def __init__(
        self, text: Optional[str] = None, children: Optional[list[Self]] = None, **attrs
    ) -> None:
        self.text = text or ""
        self.attrs = attrs
        self.children: list = children or []

    def build_attrs(self):
        attrs = ""
        if self.attrs:
            attrs = " ".join([f'{key}="{value}"' for key, value in self.attrs.items()])

        return attrs

    def render(self) -> str:
        if self.self_closing:
            return self.self_closing_render()

        inner_data = "".join([child.render() for child in self.children])
        inner_data = self.text or inner_data

        attrs = self.build_attrs()
        return f"<{self.tag_name}{' 'if attrs else ''}{attrs}>{inner_data}</{self.tag_name}>"

    def self_closing_render(self) -> str:
        attrs = self.build_attrs()
        return f"<{self.tag_name}{' 'if attrs else ''}{attrs}>"

    def add_child(self, child: Self) -> None:
        self.children.append(child)


class Doctype(TagModel):
    tag_name = "!DOCTYPE html"
    self_closing = True


class Html(TagModel):
    tag_name = "html"


class Head(TagModel):
    tag_name = "head"


class Title(TagModel):
    tag_name = "title"


class Body(TagModel):
    tag_name = "body"


class H1(TagModel):
    tag_name = "h1"


class H2(TagModel):
    tag_name = "h2"


class H3(TagModel):
    tag_name = "h3"


class H4(TagModel):
    tag_name = "h4"


class H5(TagModel):
    tag_name = "h5"


class H6(TagModel):
    tag_name = "h6"


class A(TagModel):
    tag_name = "a"


class B(TagModel):
    tag_name = "b"


class I(TagModel):
    tag_name = "i"


class P(TagModel):
    tag_name = "p"


class Link(TagModel):
    tag_name = "link"
    self_closing = True


class Style(TagModel):
    tag_name = "style"


class Div(TagModel):
    tag_name = "div"


class Svg(TagModel):
    tag_name = "svg"


class Use(TagModel):
    tag_name = "use"


class Document:
    def __init__(self, children: Optional[list[TagModel]] = None) -> None:
        self.children = children or []

    def add_child(self, child: TagModel) -> None:
        self.children.append(child)

    def render(self) -> str:
        return "".join([child.render() for child in self.children])
