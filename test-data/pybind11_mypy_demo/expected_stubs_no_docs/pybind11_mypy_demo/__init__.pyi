import os
from . import demo as demo
from typing import List, Optional, Tuple

class TestStruct:
    field_readwrite: int
    field_readwrite_docstring: int
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def field_readonly(self) -> int: ...

def func_incomplete_signature(*args, **kwargs): ...
def func_returning_optional() -> Optional[int]: ...
def func_returning_pair() -> Tuple[int, float]: ...
def func_returning_path() -> os.PathLike: ...
def func_returning_vector() -> List[float]: ...
