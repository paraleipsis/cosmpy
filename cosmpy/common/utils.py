# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Utils."""
import copy
import json
from abc import ABC
from datetime import datetime
from typing import Any


def to_isoformat(dt: datetime) -> str:
    return (
        dt.isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
        .replace(".000Z", "Z")
    )


def to_data(x: Any) -> Any:
    if hasattr(x, "to_data"):
        return x.to_data()
    if isinstance(x, int):
        return str(x)
    if isinstance(x, datetime):
        return to_isoformat(x)
    if isinstance(x, list):
        return [to_data(g) for g in x]
    if isinstance(x, dict):
        return dict_to_data(x)
    if isinstance(x, datetime):
        return to_isoformat(x)
    return x


def dict_to_data(d: dict) -> dict:
    """Recursively calls to_data on dict"""
    return {key: to_data(d[key]) for key in d}


class JSONSerializable(ABC):
    def to_data(self) -> Any:
        """Converts the object to its JSON-serializable Python data representation."""
        return dict_to_data(copy.deepcopy(self.__dict__))

    def to_json(self) -> str:
        """Marshals the object into a stringified JSON serialization. Keys are first sorted
        and the JSON rendered removes all unnecessary whitespace.

        Returns:
           str: JSON string representation
        """
        return json.dumps(self.to_data(), sort_keys=True, separators=(",", ":"))


class JSONEncoder(json.JSONEncoder):
    """JSONEncoder subclass that encode basic python objects."""  # noqa: D401

    def default(self, o: Any) -> Any:
        """Default json encode."""  # noqa: D401
        if not hasattr(o, "__json__"):
            return super().default(o)
        if callable(o.__json__):
            return o.__json__()
        return o.__json__


def json_encode(data, **kwargs):
    """Json encode."""
    return JSONEncoder(**kwargs).encode(data)
