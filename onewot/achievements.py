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
"""Entities that are used to describe achievements on WotBlitz."""

from __future__ import annotations

__all__: typing.Sequence[str] = ('BaseAchievement',)

import typing

import attr

if typing.TYPE_CHECKING:
    from onewot.internal import data_binding


class BaseAchievement:
    """Class for creating `Achievement` object."""

    def __init__(self, payload: data_binding.JSONObject) -> None:
        self.achievements = dict(
            **payload['achievements'],
            max_series=payload['max_series']
        )

    def make_class(self) -> typing.Type[object]:
        """Create a new class with user achievements data."""

        attrs = {key: attr.field() for key in self.achievements.keys()}
        return attr.make_class('Achievement', attrs=attrs, repr=True)
