from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        return [(e.name, e.value) for e in cls]
