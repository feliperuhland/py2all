from typing import TypeVar, Union


Self = TypeVar("Self", bound="TagModel")


class TagModel:
    tag_name = ""
    self_closing = False

    def __init__(self, text: Union[str, None] = None, **attrs) -> None:
        self.text = text or ""
        self.attrs = attrs
        self.children: list = []

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
