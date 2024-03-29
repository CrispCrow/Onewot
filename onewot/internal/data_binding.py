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
"""Data binding utilities."""

import typing
import enum

__all__: typing.Sequence[str] = (
    'JSONObject',
    'CLAN',
    'Language'
)

JSONObject = typing.Mapping[str, typing.Any]
"""Type hint for a JSON-decoded object representation as a mapping."""

CLAN: typing.Final[str] = 'clan'
"""Clan entity constant."""


class Language(str, enum.Enum):
    """Localization for WotBlitz API.
    
    Attributes
    ----------
    ENGLISH : typing.Final[builtins.str]
        English localization.
    RUSSIAN : typing.Final[builtins.str]
        Russian localization. Set by default.
    POLISH : typing.Final[builtins.str]
        Polish localization.
    GERMAN : typing.Final[builtins.str]
        German localization.
    FRENCH : typing.Final[builtins.str]
        French localization.
    SPANISH : typing.Final[builtins.str]
        Spanish localization.
    CHINESE_SIMPLIFIED: typing.Final[builtins.str]
        Chinese simplified localization.
    TRADITIONAL_CHINESE : typing.Final[builtins.str]
        Traditional Chinese localization.
    TURKISH : typing.Final[builtins.str]
        Turkish localization.
    CZECH : typing.Final[builtins.str]
        Czech localization.
    THAILAND : typing.Final[builtins.str]
        Thailand localization.
    VIETNAMESE : typing.Final[builtins.str]
        Vietnamese localization.
    KOREAN : typing.Final[builtins.str]
        Korean localization.
    """
    ENGLISH: typing.Final[str] = 'en'
    RUSSIAN: typing.Final[str] = 'ru'
    POLISH: typing.Final[str] = 'pl'
    GERMAN: typing.Final[str] = 'de'
    FRENCH: typing.Final[str] = 'fr'
    SPANISH: typing.Final[str] = 'es'
    CHINESE_SIMPLIFIED: typing.Final[str] = '简体中文'
    TRADITIONAL_CHINESE: typing.Final[str] = '繁體中文'
    TURKISH: typing.Final[str] = 'tr'
    CZECH: typing.Final[str] = 'cs',
    THAILAND: typing.Final[str] = 'th'
    VIETNAMESE: typing.Final[str] = 'vi'
    KOREAN: typing.Final[str] = 'ko'
