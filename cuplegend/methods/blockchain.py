from json import dumps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..main import CupLegend

from ..types import BadAPIRequest, BlockchainConfig as Config, BlockchainStats as Stats, Contract, NFT, Wallet, Rate
from ..types import Pools, Pool, TVL, TX, TXCreate, TXSign


class BlockchainMethods:
    def __init__(self, parent: "CupLegend"):
        self._parent = parent

    def config(self) -> Config | BadAPIRequest:
        """Возвращает конфигурацию блокчейна."""
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/config")

        if result["status_code"] == 200:
            return Config.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def stats(self) -> Stats | BadAPIRequest:
        """Возвращает статистику блокчейна."""
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/stats")

        if result["status_code"] == 200:
            return Stats.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def contract(self, ca: str) -> Contract | BadAPIRequest:
        """Возвращает указанный контракт.

        :param ca: Адрес контракта
        :type ca: str
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/contract/{ca}")

        if result["status_code"] == 200:
            return Contract.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def nft(self, ca: str) -> NFT | BadAPIRequest:
        """Возвращает указанный NFT.

        :param ca: Адрес контракта
        :type ca: str
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/nft/{ca}")

        if result["status_code"] == 200:
            return NFT.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def wallet(self, wallet: str) -> Wallet | BadAPIRequest:
        """Возвращает указанный кошелёк.

        :param wallet: Адрес кошелька
        :type wallet: str
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/wallet/{wallet}")

        if result["status_code"] == 200:
            return Wallet.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def rate(self, pair_1: str, pair_2: str) -> Rate | BadAPIRequest:
        """Возвращает цены указанной пары.

        :param pair_1: Адрес первой пары
        :type pair_1: str
        :param pair_2: Адрес второй пары
        :type pair_2: str
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/rate/{pair_1}/{pair_2}")

        if result["status_code"] == 200:
            return Rate.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def pools(self) -> Pools | BadAPIRequest:
        """Возвращает все доступные пулы."""
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/pools")

        if result["status_code"] == 200:
            return Pools.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def pool_by_id(self, pool_id: int) -> Pool | BadAPIRequest:
        """Возвращает указанный пул.

        :param pool_id: Идентификатор контракта
        :type pool_id: str
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/pool/{pool_id}")

        if result["status_code"] == 200:
            return Pool.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def pool_by_pairs(self, pair_1: str, pair_2: str) -> Pool | BadAPIRequest:
        """Возвращает указанный пул.

        :param pair_1: Адрес первой пары
        :type pair_1: str
        :param pair_2: Адрес второй пары
        :type pair_2: str
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/pool/{pair_1}/{pair_2}")

        if result["status_code"] == 200:
            return Pool.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def tvl(self, pair_1: str, pair_2: str, gems: bool = True) -> TVL | BadAPIRequest:
        """Возвращает TVL указанного пула.

        :param pair_1: Адрес первой пары
        :type pair_1: str
        :param pair_2: Адрес второй пары
        :type pair_2: str
        :param gems: Валюта TVL
        :type gems: bool
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/tvl/{pair_1}/{pair_2}?gems={gems}")

        if result["status_code"] == 200:
            return TVL.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def get_tx(self, tx_id: int) -> TX | BadAPIRequest:
        """Возвращает указанную транзакцию.

        :param tx_id: Идентификатор транзакции
        :type tx_id: int
        """
        # noinspection PyProtectedMember
        result = self._parent._api_call(url=f"blockchain/tx/get/{tx_id}")

        if result["status_code"] == 200:
            return TX.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def create_tx(self, data: dict) -> TXCreate | BadAPIRequest:
        """Создаёт транзакцию с указанными мета-данными.

        :param data: Тело транзакции
        :type data: dict
        """
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(method="post",
                                        url=f"blockchain/tx/create/{self._parent._token}",
                                        data=dumps(data))

        if result["status_code"] == 200:
            return TXCreate.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)

    def sign_tx(self, tx_id: int, seed: str) -> TXSign | BadAPIRequest:
        """Подписывает указанную транзакцию.

        :param tx_id: Идентификатор транзакции
        :type tx_id: int
        :param seed: Сид-фраза кошелька
        :type seed: str
        """
        # noinspection PyProtectedMember
        if not self._parent._token:
            raise Exception("Для использования этого метода требуется создать объект с действующим API-ключом.")

        # noinspection PyProtectedMember
        result = self._parent._api_call(method="post",
                                        url=f"blockchain/tx/sign/{self._parent._token}",
                                        data=dumps({"tx_id": tx_id,
                                                    "seed": seed}))

        if result["status_code"] == 200:
            return TXSign.model_validate(result)
        else:
            return BadAPIRequest.model_validate(result)
