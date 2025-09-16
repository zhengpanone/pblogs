from typing import Protocol, TypeVar, Generic, overload

T = TypeVar("T", contravariant=True)   # 拥有者类型（Rectangle），只能出现在输入位置
V = TypeVar("V")                       # 值类型（float）

class Descriptor(Protocol[T, V]):
    def __get__(self, instance: T, owner: type[T]) -> V: ...
    def __set__(self, instance: T, value: V) -> None: ...


class PositiveNumber(Generic[T, V]):
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    @overload
    def __get__(self, instance: None, owner: type[T]) -> "PositiveNumber[T, V]": ...
    
    @overload
    def __get__(self, instance: T, owner: type[T]) -> V: ...

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value: V):
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                f"{self.private_name[1:].capitalize()} must be a positive number"
            )
        setattr(instance, self.private_name, value)


class Rectangle:
    width: Descriptor["Rectangle", float] = PositiveNumber()
    height: Descriptor["Rectangle", float] = PositiveNumber()

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @property
    def diagonal(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5

    @property
    def is_square(self) -> bool:
        return self.width == self.height

    @property
    def is_rectangle(self) -> bool:
        return self.width != self.height


if __name__ == "__main__":
    r = Rectangle(10, 20)
    print(r.area)
    print(r.perimeter)
    print(r.diagonal)
    print(r.is_square)
    print(r.is_rectangle)

    r.width = 30
    print(r.area)
    print(r.perimeter)
    print(r.diagonal)
    print(r.is_square)
    print(r.is_rectangle)
