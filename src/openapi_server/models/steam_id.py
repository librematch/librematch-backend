# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SteamId(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SteamId - a model defined in OpenAPI

        _self: The _self of this SteamId.
    """

    _self: int = Field(alias="self")

    @validator("_self")
    def _self_max(cls, value):
        assert value <= 18
        return value

    @validator("_self")
    def _self_min(cls, value):
        assert value >= 14
        return value

SteamId.update_forward_refs()