# -*- coding: utf-8 -*-
# cython: language_level=3
# Copyright (c) 2022 Crisp Crow
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Interface for an error handler for WotBlitz API"""

from __future__ import annotations

__all__: typing.Sequence[str] = ('ErrorHandler',)

import typing
import abc

if typing.TYPE_CHECKING:
    from onewot.internal import data_binding
    from onewot import errors


class ErrorHandler(abc.ABC):
    """Interface for handling WotBlitz API JSON responses."""

    @abc.abstractmethod
    def handle(
        self,
        payload: data_binding.JSONObject,
        params: dict[str, typing.Any]
    ) -> typing.Union[data_binding.JSONObject, errors.OnewotError]:
        """Handle recieved JSON object.

        Parameters
        ----------
        payload : onewot.internal.data_binding.JSONObject
            The JSON payload to handle.
        params : builtins.dict[builtins.str, typing.Any]
            Parameters of HTTP request body.

        Returns
        -------
        typing.Optional[onewot.internal.data_binding.JSONObject]
            The JSON payload.
        onewot.errors.OnewotError
            if API request response returns JSON payload with status `error`
        """
