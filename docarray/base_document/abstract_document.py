from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, Type, TypeVar

from pydantic.fields import ModelField

if TYPE_CHECKING:
    from pydantic.typing import SetStr

    from docarray.base_document.mixins.proto import ProtoMixin


T = TypeVar('T', bound='AbstractDocument')


class AbstractDocument(Iterable):
    __fields__: Dict[str, ModelField]

    @classmethod
    @abstractmethod
    def _get_field_type(cls, field: str) -> Type['ProtoMixin']:
        ...

    @classmethod
    @abstractmethod
    def construct(
        cls: Type[T], _fields_set: Optional['SetStr'] = None, **values: Any
    ) -> T:
        """
        construct document without calling validation
        """
        ...

    @classmethod
    @abstractmethod
    def smart_parse_obj(cls: Type[T], obj: Dict[str, Any]) -> T:
        ...
