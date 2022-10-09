# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class NotFoundError(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NotFoundError - a model defined in OpenAPI

        message: The message of this NotFoundError.
        code: The code of this NotFoundError.
    """

    message: str = Field(alias="message")
    code: int = Field(alias="code")

    @validator("code")
    def code_max(cls, value):
        assert value <= 404
        return value

    @validator("code")
    def code_min(cls, value):
        assert value >= 404
        return value

NotFoundError.update_forward_refs()