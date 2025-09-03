from .types import *

from json import dumps
from requests import request


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
        """Возвращает информацию о клане.

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


class CupLegend:
    def __init__(self, api_key: str = None):
        """Создаёт объект для обращения к API-методам Cup Legend.

        :param api_key: API-ключ (опционально)
        :type api_key: str
        """
        self._url = "https://api.cuplegend.ru"
        self._token: str | None = api_key

        self.base = BaseMethods(self)
        self.info = InfoMethods(self)
        self.app = AppMethods(self)
        self.checks = ChecksMethods(self)
        self.invoices = InvoicesMethods(self)

    def _api_call(self, url: str = "", method: str = "get", data: str = None) -> any:
        return request(method=method, url=f"{self._url}/{url}", data=data).json()
