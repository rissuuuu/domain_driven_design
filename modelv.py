from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple
import pytest
from _pytest.outcomes import Failed


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str

dataclass(frozen=True)
class Money:
    currency: str
    value: int

    def __add__(self,other) -> Money:
        if other.currency != self.currency:
            raise ValueError(f"Cannot add {self.currency} to {other.currency}")
        return Money(self.currency,self.value+other.value)

npr= Money('npr',10)
inr=Money('inr',20)