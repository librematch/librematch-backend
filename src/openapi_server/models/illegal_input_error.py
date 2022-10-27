# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IllegalInputError(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IllegalInputError - a model defined in OpenAPI

        message: The message of this IllegalInputError.
        code: The code of this IllegalInputError.
    """

    message: str = Field(alias="message")
    code: int = Field(alias="code")

    @validator("message")
    def message_max_length(cls, value):
        assert len(value) <= 32
        return value

    @validator("message")
    def message_pattern(cls, value):
        assert value is not None and re.match(r"^example-[0-9a-z]+$", value)
        return value

    @validator("code")
    def code_max(cls, value):
        assert value <= 400
        return value

    @validator("code")
    def code_min(cls, value):
        assert value >= 400
        return value

IllegalInputError.update_forward_refs()
