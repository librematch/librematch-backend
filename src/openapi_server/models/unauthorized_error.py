# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UnauthorizedError(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UnauthorizedError - a model defined in OpenAPI

        message: The message of this UnauthorizedError.
        code: The code of this UnauthorizedError.
    """

    message: str = Field(alias="message")
    code: int = Field(alias="code")

    @validator("code")
    def code_max(cls, value):
        assert value <= 401
        return value

    @validator("code")
    def code_min(cls, value):
        assert value >= 401
        return value

UnauthorizedError.update_forward_refs()
