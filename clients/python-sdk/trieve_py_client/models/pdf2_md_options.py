# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.13.0
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Pdf2MdOptions(BaseModel):
    """
    Pdf2MdOptions
    """ # noqa: E501
    split_headings: Optional[StrictBool] = Field(default=None, description="Split headings is an optional field which allows you to specify whether or not to split headings into separate chunks. Default is false.")
    system_prompt: Optional[StrictStr] = Field(default=None, description="Prompt to use for the gpt-4o model. Default is None.")
    use_pdf2md_ocr: StrictBool = Field(description="Parameter to use pdf2md_ocr. If true, the file will be converted to markdown using gpt-4o. Default is false.")
    __properties: ClassVar[List[str]] = ["split_headings", "system_prompt", "use_pdf2md_ocr"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Pdf2MdOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if split_headings (nullable) is None
        # and model_fields_set contains the field
        if self.split_headings is None and "split_headings" in self.model_fields_set:
            _dict['split_headings'] = None

        # set to None if system_prompt (nullable) is None
        # and model_fields_set contains the field
        if self.system_prompt is None and "system_prompt" in self.model_fields_set:
            _dict['system_prompt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Pdf2MdOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "split_headings": obj.get("split_headings"),
            "system_prompt": obj.get("system_prompt"),
            "use_pdf2md_ocr": obj.get("use_pdf2md_ocr")
        })
        return _obj


