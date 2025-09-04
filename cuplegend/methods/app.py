from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..main import CupLegend


from json import dumps

from ..types import BadAPIRequest, AppInvoices, SendGift, AppInfo, GetStorage, SetStorage, ClearStorage


class StorageMethods:
    def __init__(self, parent: "AppMethods"):
        self._parent = parent

    def get(self) -> GetStorage | BadAPIRequest:
        """Возвращает хранилище приложения."""
        # noinspection PyProtectedMember
        if not self._parent._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._parent._api_call(url=f"app/storage/get/{self._parent._parent._token}")

        if result["status_code"] == 200:
            return GetStorage.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def set(self, storage: dict) -> SetStorage | BadAPIRequest:
        """Обновляет хранилище приложения.

        :param storage: Словарь (dict) с данными
        :type storage: dict
        """
        # noinspection PyProtectedMember
        if not self._parent._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._parent._api_call(method="post",
                                                url=f"app/storage/set/{self._parent._parent._token}",
                                                data=dumps(storage))

        if result["status_code"] == 200:
            return SetStorage.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def clear(self) -> ClearStorage | BadAPIRequest:
        """Очищает хранилище приложения."""
        # noinspection PyProtectedMember
        if not self._parent._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._parent._api_call(method="delete",
                                                url=f"app/storage/clear/{self._parent._parent._token}")

        if result["status_code"] == 200:
            return ClearStorage.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)


class AppMethods:
    def __init__(self, parent: "CupLegend"):
        self._parent = parent

        self.storage = StorageMethods(self)

    def myself(self) -> AppInfo | BadAPIRequest:
        """Возвращает информацию о приложении."""
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"app/myself/{self._parent._token}")

        if result["status_code"] == 200:
            return AppInfo.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def invoices(self) -> AppInvoices | BadAPIRequest:
        """Возвращает информацию о созданных счетах."""
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"app/invoices/{self._parent._token}")

        if result["status_code"] == 200:
            return AppInvoices.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def send_gift(self, UGID: int, UUID: int) -> SendGift | BadAPIRequest:
        """Отправляет указанный подарок на указанный аккаунт."""
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(method="post",
                                        url=f"app/send_gift/{self._parent._token}/{UGID}/{UUID}")

        if result["status_code"] == 200:
            return SendGift.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)
