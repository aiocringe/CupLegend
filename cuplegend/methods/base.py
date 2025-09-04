from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..main import CupLegend

from ..types import Info, BadAPIRequest, Stats


class BaseMethods:
    def __init__(self, parent: "CupLegend"):
        self._parent = parent

    def info(self) -> Info | BadAPIRequest:
        """Возвращает информацию о боте."""
        # noinspection PyProtectedMember
        result = self._parent._api_call()

        if result["status_code"] == 200:
            return Info.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def stats(self) -> Stats | BadAPIRequest:
        """Возвращает статистику бота."""
        # noinspection PyProtectedMember
        result = self._parent._api_call(url="stats")

        if result["status_code"] == 200:
            return Stats.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)
