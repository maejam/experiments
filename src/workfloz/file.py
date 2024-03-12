from __future__ import annotations

from abc import ABC, abstractmethod


class Myclass(ABC):
    @abstractmethod
    def mymeth(self) -> None:
        pass


a = 1
b = "toto"
c = 42
d=54


def my_func() -> int:
    return 1
