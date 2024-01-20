# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
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

"""Implementation of REST api client."""
import asyncio
import base64
import json
from typing import List, Optional
from urllib.parse import urlencode

import requests
import aiohttp
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message
from requests import Response


class RestClient:
    """REST api client."""

    def __init__(self, rest_address: str):
        """
        Create REST api client.

        :param rest_address: Address of REST node
        """
        self._session = requests.session()
        self.rest_address = rest_address

    @staticmethod
    def hard_fix_response(
            response: Response
    ) -> bytes:
        res = response.json()

        if "tip" in res.get("tx", {}).get("auth_info", {}):
            del res['tx']['auth_info']['tip']

        tx_response = res.get("tx_response", {}).get("tx")
        if tx_response:
            if "tip" in tx_response.get("auth_info", {}):
                del res['tx_response']['tx']['auth_info']['tip']

        if "events" in res.get("result", {}):
            res["result"]["events"] = []

        if "events" in res.get("tx_response", {}):
            res["tx_response"]["events"] = []

        if "msg_responses" in res.get("result", {}):
            del res["result"]["msg_responses"]

        response = json.dumps(res).encode()

        return response

    def get(
            self,
            url_base_path: str,
            request: Optional[Message] = None,
            used_params: Optional[List[str]] = None,
        ) -> bytes:
            """
            Send a GET request.

            :param url_base_path: URL base path
            :param request: Protobuf coded request
            :param used_params: Parameters to be removed from request after converting it to dict

            :raises RuntimeError: if response code is not 200

            :return: Content of response
            """
            url = self._make_url(
                url_base_path=url_base_path, request=request, used_params=used_params
            )

            response = self._session.get(url=url)
            if response.status_code != 200:
                raise RuntimeError(
                    f"Error when sending a GET request.\n Response: {response.status_code}, {str(response.content)})"
                )

            response = self.hard_fix_response(response)

            return response

    def _make_url(
        self,
        url_base_path: str,
        request: Optional[Message] = None,
        used_params: Optional[List[str]] = None,
    ) -> str:
        """
        Construct URL for get request.

        :param url_base_path: URL base path
        :param request: Protobuf coded request
        :param used_params: Parameters to be removed from request after converting it to dict

        :return: URL string
        """
        json_request = MessageToDict(request) if request else {}

        # Remove params that are already in url_base_path
        for param in used_params or []:
            json_request.pop(param)

        url_encoded_request = self._url_encode(json_request)

        url = f"{self.rest_address}{url_base_path}"
        if url_encoded_request:
            url = f"{url}?{url_encoded_request}"

        return url

    def post(self, url_base_path: str, request: Message) -> bytes:
        """
        Send a POST request.

        :param url_base_path: URL base path
        :param request: Protobuf coded request

        :raises RuntimeError: if response code is not 200

        :return: Content of response
        """
        json_request = MessageToDict(request)

        # Workaround
        if "tx" in json_request:
            if "body" in json_request["tx"]:
                if "messages" in json_request["tx"]["body"]:
                    for message in json_request["tx"]["body"]["messages"]:
                        if "msg" in message:
                            message["msg"] = json.loads(
                                base64.b64decode(message["msg"])
                            )

        headers = {"Content-type": "application/json", "Accept": "application/json"}
        response = self._session.post(
            url=f"{self.rest_address}{url_base_path}",
            json=json_request,
            headers=headers,
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Error when sending a POST request.\n Request: {json_request}\n Response: {response.status_code}, {str(response.content)})"
            )

        response = self.hard_fix_response(response)

        return response

    @staticmethod
    def _url_encode(json_request):
        """A Custom URL encodes that breaks down nested dictionaries to match REST api format.

        It converts dicts from:
        {"pagination": {"limit": "1", "something": "2"},}

        To:
        {"pagination.limit": "1","pagination.something": "2"}


        :param json_request: JSON request

        :return: urlencoded json_request
        """  # noqa: D401
        for outer_k, outer_v in json_request.copy().items():
            if isinstance(outer_v, dict):
                for inner_k, inner_v in outer_v.items():
                    json_request[f"{outer_k}.{inner_k}"] = inner_v
                json_request.pop(outer_k)

        return urlencode(json_request, doseq=True)

    def __del__(self):
        """Destructor method."""
        self._session.close()


class AsyncRestClient:
    """REST api client."""

    def __init__(self, rest_address: str):
        """
        Create REST api client.

        :param rest_address: Address of REST node
        """
        self.rest_address = rest_address

    @staticmethod
    async def hard_fix_response(
            response: aiohttp.ClientResponse
    ) -> bytes:
        res = await response.json(content_type=None)

        if "tip" in res.get("tx", {}).get("auth_info", {}):
            del res['tx']['auth_info']['tip']

        tx_response = res.get("tx_response", {}).get("tx")
        if tx_response:
            if "tip" in tx_response.get("auth_info", {}):
                del res['tx_response']['tx']['auth_info']['tip']

        if "events" in res.get("result", {}):
            res["result"]["events"] = []

        if "events" in res.get("tx_response", {}):
            res["tx_response"]["events"] = []

        if "msg_responses" in res.get("result", {}):
            del res["result"]["msg_responses"]

        response = json.dumps(res).encode()

        return response

    async def get(
            self,
            url_base_path: str,
            request: Optional[Message] = None,
            used_params: Optional[List[str]] = None,
        ) -> bytes:
            """
            Send a GET request.

            :param url_base_path: URL base path
            :param request: Protobuf coded request
            :param used_params: Parameters to be removed from request after converting it to dict

            :raises RuntimeError: if response code is not 200

            :return: Content of response
            """
            url = self._make_url(
                url_base_path=url_base_path, request=request, used_params=used_params
            )

            async with aiohttp.ClientSession() as session:
                response = await session.get(url=url)

                if response.status != 200:
                    raise RuntimeError(
                        f"Error when sending a GET request.\n Response: {response.status}, {await response.text()})"
                    )

                response = await self.hard_fix_response(response)

            return response

    def _make_url(
        self,
        url_base_path: str,
        request: Optional[Message] = None,
        used_params: Optional[List[str]] = None,
    ) -> str:
        """
        Construct URL for get request.

        :param url_base_path: URL base path
        :param request: Protobuf coded request
        :param used_params: Parameters to be removed from request after converting it to dict

        :return: URL string
        """
        json_request = MessageToDict(request) if request else {}

        # Remove params that are already in url_base_path
        for param in used_params or []:
            json_request.pop(param)

        url_encoded_request = self._url_encode(json_request)

        url = f"{self.rest_address}{url_base_path}"
        if url_encoded_request:
            url = f"{url}?{url_encoded_request}"

        return url

    async def post(self, url_base_path: str, request: Message) -> bytes:
        """
        Send a POST request.

        :param url_base_path: URL base path
        :param request: Protobuf coded request

        :raises RuntimeError: if response code is not 200

        :return: Content of response
        """
        json_request = MessageToDict(request)

        # Workaround
        if "tx" in json_request:
            if "body" in json_request["tx"]:
                if "messages" in json_request["tx"]["body"]:
                    for message in json_request["tx"]["body"]["messages"]:
                        if "msg" in message:
                            message["msg"] = json.loads(
                                base64.b64decode(message["msg"])
                            )

        headers = {"Content-type": "application/json", "Accept": "application/json"}
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                url=f"{self.rest_address}{url_base_path}",
                json=json_request,
                headers=headers,
            )

            if response.status != 200:
                raise RuntimeError(
                    f"Error when sending a POST request.\n Request: {json_request}\n Response: {response.status}, {await response.text()})"
                )

            response = await self.hard_fix_response(response)

        return response

    @staticmethod
    def _url_encode(json_request):
        """A Custom URL encodes that breaks down nested dictionaries to match REST api format.

        It converts dicts from:
        {"pagination": {"limit": "1", "something": "2"},}

        To:
        {"pagination.limit": "1","pagination.something": "2"}


        :param json_request: JSON request

        :return: urlencoded json_request
        """  # noqa: D401
        for outer_k, outer_v in json_request.copy().items():
            if isinstance(outer_v, dict):
                for inner_k, inner_v in outer_v.items():
                    json_request[f"{outer_k}.{inner_k}"] = inner_v
                json_request.pop(outer_k)

        return urlencode(json_request, doseq=True)
