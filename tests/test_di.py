import dataclasses
from dataclasses import dataclass

import pytest

from batchbald_redux.di import DependencyInjection


def test_di_simple_type():
    @dataclass
    class SimpleType:
        a_config_variable: int


    di = DependencyInjection(dict(a_config_variable=5))

    instance = di.create_dataclass_type(SimpleType)

    assert instance.a_config_variable == 5


def test_di_simple_type_with_default():
    @dataclass
    class SimpleType:
        a_config_variable: int = 5

    di = DependencyInjection(dict())

    instance = di.create_dataclass_type(SimpleType)

    assert instance.a_config_variable == 5


def test_di_simple_type_with_default_factory():
    @dataclass
    class SimpleType:
        a_config_variable: int = dataclasses.field(default_factory=lambda: 5)

    di = DependencyInjection(dict())

    instance = di.create_dataclass_type(SimpleType)

    assert instance.a_config_variable == 5

@dataclass
class SimpleTypeA:
    a_config_variable: int


@dataclass
class SimpleTypeB:
    a_config_variable: int


def test_di_annotated_type():
    print(SimpleTypeB.__qualname__)
    di = DependencyInjection(dict(a_config_variable=5, SimpleTypeB__a_config_variable=10))

    instance_a = di.create_dataclass_type(SimpleTypeA)
    instance_b = di.create_dataclass_type(SimpleTypeB)

    assert instance_a.a_config_variable == 5
    assert instance_b.a_config_variable == 10


def test_di_nested_types():
    @dataclass
    class ComplexTypeC:
        simple_type_b: SimpleTypeB


    di = DependencyInjection(dict(SimpleTypeB__a_config_variable=10), [SimpleTypeB])

    instance_c = di.create_dataclass_type(ComplexTypeC)

    assert instance_c.simple_type_b.a_config_variable == 10


def test_di_nested_types_raises_without_support():
    @dataclass
    class SimpleTypeB:
        a_config_variable: int


    @dataclass
    class ComplexTypeC:
        simple_type_b: SimpleTypeB


    # Trigger a missing fields error
    di = DependencyInjection(dict(SimpleTypeB__a_config_variable=10), [])

    with pytest.raises(ValueError):
        di.create_dataclass_type(ComplexTypeC)
