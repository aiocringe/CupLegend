from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..main import CupLegend

from ..types import BadAPIRequest, InvoiceCreate, InvoiceDelete, InvoiceInfo


class InvoicesMethods:
    def __init__(self, parent: "CupLegend"):
        self._parent = parent

    def get(self, code: str) -> InvoiceInfo | BadAPIRequest:
        """Возвращает указанный счёт.

        :param code: Код счёта
        :type code: str
        """
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"invoices/get/{self._parent._token}/{code}")

        if result["status_code"] == 200:
            return InvoiceInfo.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def create(self, payments: int, summa: int, comment: bool = False) -> InvoiceCreate | BadAPIRequest:
        """Создаёт счёт с указанной суммой оплаты для указанного количества оплат.

        :param payments: Количество оплат
        :type payments: int
        :param summa: Сумма оплаты
        :type summa: int
        :param comment: Комментарии к оплате
        :type comment: bool
        """
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(method="post",
                                        url=f"invoices/create/{self._parent._token}/{payments}/{summa}?comment={comment}")

        if result["status_code"] == 200:
            return InvoiceCreate.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def delete(self, code: str) -> InvoiceDelete | BadAPIRequest:
        """Удаляет указанный счёт.

        :param code: Код счёта
        :type code: str
        """
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(method="delete",
                                        url=f"invoices/delete/{self._parent._token}/{code}")

        if result["status_code"] == 200:
            return InvoiceDelete.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)
