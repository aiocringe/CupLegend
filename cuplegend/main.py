from .methods import *

from requests import request

class CupLegend:
    def __init__(self, api_key: str = None):
        """Создаёт объект для обращения к API-методам Cup Legend.

        :param api_key: API-ключ (опционально)
        :type api_key: str
        """
        self._url = "https://api.cuplegend.ru"
        self._token: str | None = api_key

        self.base: BaseMethods = BaseMethods(self)
        self.info: InfoMethods = InfoMethods(self)
        self.app: AppMethods = AppMethods(self)
        self.blockchain: BlockchainMethods = BlockchainMethods(self)
        self.checks: ChecksMethods = ChecksMethods(self)
        self.invoices: InvoicesMethods = InvoicesMethods(self)

    def _api_call(self, url: str = "", method: str = "get", data: str = None) -> dict:
        return request(method=method, url=f"{self._url}/{url}", data=data).json()
