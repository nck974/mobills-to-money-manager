"""
Mobills models
"""
from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, validator

from model.transaction import TransactionType


class MobillsTransaction(BaseModel):
    """
    Representation of the data exported by Mobills
    """

    transaction_type: TransactionType
    date: datetime
    description: str
    value: float
    category: str
    subcategory: Optional[str] = None
    tags: Optional[str] = None
    account: Optional[str] = None

    @validator("*", pre=False)
    @classmethod
    def set_empty_to_none(cls, value: Any) -> Any | None:
        """
        Set the values that are empty to none instead of an empty string
        """
        if isinstance(value, str) and value == "":
            return None
        return value
