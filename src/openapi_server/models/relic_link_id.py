# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class RelicLinkId(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RelicLinkId - a model defined in OpenAPI

        relic_link_id: The relic_link_id of this RelicLinkId.
    """

    relic_link_id: int = Field(alias="relic_link_id")

    @validator("relic_link_id")
    def relic_link_id_max(cls, value):
        assert value <= 999999999
        return value

    @validator("relic_link_id")
    def relic_link_id_min(cls, value):
        assert value >= 0
        return value

RelicLinkId.update_forward_refs()
