from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..main import CupLegend

from ..types import BadAPIRequest, Hero, StarBox, Gifts, Gift, Clan, Account


class InfoMethods:
    def __init__(self, parent: "CupLegend"):
        self._parent = parent

    def account(self, UUID: int) -> Account | BadAPIRequest:
        """Возвращает информацию об аккаунте.

        :param UUID: Идентификатор игрока
        :type UUID: int"""
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"account/{UUID}")

        if result["status_code"] == 200:
            return Account.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def clan(self, UCID: int) -> Clan | BadAPIRequest:
        """Возвращает информацию о клане.

        :param UCID: Идентификатор клана
        :type UCID: int
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"clan/{UCID}")

        if result["status_code"] == 200:
            return Clan.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def gift(self, UGID: int) -> Gift | BadAPIRequest:
        """Возвращает информацию о подарке.

        :param UGID: Идентификатор подарка
        :type UGID: int
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"gift/{UGID}")

        if result["status_code"] == 200:
            return Gift.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def user_gifts(self, UUID: int) -> Gifts | BadAPIRequest:
        """Возвращает информацию о подарках игрока.

        :param UUID: Идентификатор игрока
        :type UUID: int
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"gifts/{UUID}")

        if result["status_code"] == 200:
            return Gifts.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def hero(self, UHID: int) -> Hero | BadAPIRequest:
        """Возвращает информацию о персонаже.

        :param UHID: Идентификатор персонажа
        :type UHID: int
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"hero/{UHID}")

        if result["status_code"] == 200:
            return Hero.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def star_box(self, UBID: int) -> StarBox | BadAPIRequest:
        """Возвращает информацию о StarBox.

        :param UBID: Идентификатор StarBox
        :type UBID: int
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"sb/{UBID}")

        if result["status_code"] == 200:
            return StarBox.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)
