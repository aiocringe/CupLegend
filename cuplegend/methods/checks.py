from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..main import CupLegend

from ..types import BadAPIRequest, CheckDelete, CheckCreate


class ChecksMethods:
    def __init__(self, parent: "CupLegend"):
        self._parent = parent

    def create(self, activations: int, reward: int) -> CheckCreate | BadAPIRequest:
        """Создаёт чек с указанной наградой для указанного количества активаций.

        :param activations: Количество активаций
        :type activations: int
        :param reward: Награда за активацию
        :type reward: int
        """
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(method="post",
                                        url=f"checks/create/{self._parent._token}/{activations}/{reward}")

        if result["status_code"] == 200:
            return CheckCreate.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def delete(self, code: str) -> CheckDelete | BadAPIRequest:
        """Удаляет указанный чек.

        :param code: Код чека
        :type code: str
        """
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(method="delete",
                                        url=f"checks/delete/{self._parent._token}/{code}")

        if result["status_code"] == 200:
            return CheckDelete.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)
