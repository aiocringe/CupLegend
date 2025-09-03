from pydantic import BaseModel


# Базовые типы объектов

class BadAPIRequest(BaseModel):
    status_code: int
    msg: str


class DateTime(BaseModel):
    date: str
    time: str


class GiftMetaData(BaseModel):
    collection: int
    link: str
    name: str
    ticker: str
    rare: str
    supply: int | str
    price: int


class GiftModel(BaseModel):
    name: str
    number: int
    chance: int
    upgraded: DateTime
    gift_link: str


# Методы API

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
