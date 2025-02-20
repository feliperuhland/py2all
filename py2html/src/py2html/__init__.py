from typing import TypeVar, Union

Self = TypeVar("Self", bound="Tag")


class Tag:
    def __init__(
        self,
        name: str,
        inner_data: Union[Self, str, None] = None,
        self_closing_tag: bool = False,
        **attrs,
    ) -> None:
        self.name = name
        self.inner_data = inner_data
        self.self_closing_tag = self_closing_tag
        self.attrs = attrs

    def export(self) -> str:
        attrs = ""
        if self.attrs:
            attrs = " ".join([f'{key}="{value}"' for key, value in self.attrs.items()])

        if self.self_closing_tag:
            return f"<{self.name}{' 'if attrs else ''}{attrs}>"

        inner_data = ""
        if isinstance(self.inner_data, str):
            inner_data = self.inner_data
        elif isinstance(self.inner_data, Tag):
            inner_data = self.inner_data.export()

        return f"<{self.name}{' 'if attrs else ''}{attrs}>{inner_data}</{self.name}>"


__all__ = ["Tag"]
