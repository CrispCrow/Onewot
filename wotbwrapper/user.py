from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar, Generic

__all__ = ('User')

T = TypeVar('T')

class Timestamp(Generic[T]):
	...


class BaseUser:
	__slots__ = (
		'id',
		'clan_id',
		'client_language',
		'created_at',
		'global_rating',
		'last_battle_time',
		'logout_at',
		'nickname',
		'updated_at',
	)

	if TYPE_CHECKING:
		id: int
		clan_id: int
		client_language: str
		created_at: Timestamp[datetime.datetime]
		global_rating: int
		last_battle_time: Timestamp[datetime.datetime]
		logout_at: Timestamp[datetime.datetime]
		nickname: str
		updated_at: Timestamp[datetime.datetime]


class User(BaseUser):
	pass