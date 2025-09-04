from .base_types import *


class Info(BaseModel):
    status_code: int
    name: str
    id: int
    username: str
    news: str
    chat: str


class Stats(BaseModel):
    status_code: int
    players: int
    online: int
    chats: int
    duels: int
    cup_up: int
    trophies: int
    rubles: int
    tokens: int
    gems: int


class Account(BaseModel):
    class _Social(BaseModel):
        karma: int
        mark: str

    status_code: int
    UUID: int
    clan: int
    level: int
    trophies: int
    nickname: str
    privilege: str
    social: _Social
    reg_date: DateTime
    online: DateTime


class Clan(BaseModel):
    class _ClanMember(BaseModel):
        nickname: str
        date: str
        time: str
        stars: int

    status_code: int
    UCID: int
    name: str
    leader: int
    level: int
    create_date: DateTime
    description: str
    rating: int
    members: dict[str, _ClanMember]


class Gift(BaseModel):
    status_code: int
    owner: int
    sender: int
    received: DateTime
    meta: GiftMetaData
    model: GiftModel | dict


class Gifts(BaseModel):
    class _GiftInfo(BaseModel):
        sender: int
        received: DateTime
        meta: GiftMetaData
        model: GiftModel | dict

    status_code: int
    gifts: dict[str, _GiftInfo]


class Hero(BaseModel):
    status_code: int
    creator: int
    UHID: int
    name: str
    description: str
    religion: str
    wins: int
    loses: int
    level: int
    trophies: int
    create_date: DateTime


class StarBox(BaseModel):
    class _StarBoxMeta(BaseModel):
        experience: int
        gems: int
        trophies: int
        tokens: int
        fragments: int
        energy: int
        privilege: str
        rune: str
        artifact: str
        weapons: list[str]

    status_code: int
    opener: int
    rare: str
    date: DateTime
    link: str
    meta: _StarBoxMeta


class AppInfo(BaseModel):
    status_code: int
    UUID: int
    UAID: int
    name: str
    balance: int
    checks: int
    invoices: int


class AppInvoices(BaseModel):
    class _InvoiceInfo(BaseModel):
        payments: int
        amount: int

    status_code: int
    invoices: dict[str, _InvoiceInfo]


class GetStorage(BaseModel):
    status_code: int
    storage: dict


class SetStorage(BaseModel):
    status_code: int


class ClearStorage(BaseModel):
    status_code: int


class SendGift(BaseModel):
    status_code: int


class BlockchainConfig(BaseModel):
    status_code: int
    contract: str
    fee: float
    available_tx_types: list[str]
    price_channel: int
    max_token_supply: int


class BlockchainStats(BaseModel):
    status_code: int
    total_tx: int
    total_confirmed_tx: int
    tps: dict[str, float | None]
    tx_stats: dict[str, dict[str, int]]


class Contract(BaseModel):
    status_code: int
    master: str | None = None
    type: str
    init: float | int
    name: str
    ticker: str | None = None
    channel: int
    supply: float | int
    max_supply: float | None = None
    fee: float | None = None
    attributes: list[str] | None = None
    honeypot: bool | None = None
    honeypot_reverse: bool | None = None
    soulbound: bool | None = None
    verification: bool


class NFT(BaseModel):
    status_code: int
    contract: str
    collection: str
    sequence: int
    attributes: dict[str, str | int | float]
    format: str
    owner: str


class Wallet(BaseModel):
    status_code: int
    tokens: dict[str, float | int] | dict
    lp: dict[str, float | int] | dict
    nft: list[str] | list


class Rate(BaseModel):
    status_code: int
    first_rate: float | int
    second_rate: float | int


class Pools(BaseModel):
    status_code: int
    pools: dict[str, dict[str, list[list[dict[str, str | None]]] | dict[str, float | int]]]


class Pool(BaseModel):
    status_code: int
    pool_id: int
    pool_address: str
    pair_1: dict[str, str | float | int]
    pair_2: dict[str, str | float | int]


class TVL(BaseModel):
    status_code: int
    tvl: float | int


class TX(BaseModel):
    status_code: int
    status: int
    type: str
    wallet: str
    fee: float | int
    init: float
    launched: float | None = None
    finished: float | None = None
    duration: float | None = None
    token: str | None = None
    master: str | None = None
    new_owner: str | None = None
    gift_id: int | None = None
    market: str | float | int | None = None
    pool: str | None = None
    ca: str | None = None
    contract: str | None = None
    collection: str | None = None
    domain: str | None = None
    pair: str | None = None
    sent: float | int | None = None
    received: float | int | None = None
    receivers: list[str] | None = None
    message: str | None = None
    old_rate: float | int | None = None
    new_rate: float | int | None = None
    token_old_rate: float | int | None = None
    token_new_rate: float | int | None = None
    pair_old_rate: float | int | None = None
    pair_new_rate: float | int | None = None
    percent: float | int | None = None
    lot: str | int | None = None
    nft: str | None = None
    summa: int | float | None = None
    price: int | float | None = None
    summa_1: int | float | None = None
    summa_2: int | float | None = None
    pair_1: int | float | None = None
    pair_2: int | float | None = None
    lp: int | float | None = None


class TXCreate(BaseModel):
    status_code: int
    tx_id: int


class TXSign(BaseModel):
    status_code: int


class CheckCreate(BaseModel):
    status_code: int
    code: str
    link: str


class CheckDelete(BaseModel):
    status_code: int


class InvoiceInfo(BaseModel):
    class _Payment(BaseModel):
        date: DateTime
        summa: int
        comment: str

    status_code: int
    payed: bool
    payments: dict[str, dict[str, _Payment]] | dict


class InvoiceCreate(BaseModel):
    status_code: int
    code: str
    link: str


class InvoiceDelete(BaseModel):
    status_code: int
