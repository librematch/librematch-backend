# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SearchParam(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SearchParam - a model defined in OpenAPI

        _self: The _self of this SearchParam.
    """

    _self: str = Field(alias="self")

    @validator("_self")
    def _self_max_length(cls, value):
        assert len(value) <= 10
        return value

    @validator("_self")
    def _self_pattern(cls, value):
        assert value is not None and re.match(r"^.{10}$", value)
        return value

SearchParam.update_forward_refs()
