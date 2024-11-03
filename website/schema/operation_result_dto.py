
from pydantic import BaseModel
from typing import Generic, Optional, TypeVar

T = TypeVar('T')
class ExceptionModel(BaseModel):
    detail: Optional[str] = None
    status_code: Optional[int] = None

class OperationResult(BaseModel, Generic[T]):
    is_success: bool
    exception: Optional[ExceptionModel] = None
    data: Optional[T] = None