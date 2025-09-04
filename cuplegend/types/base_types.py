from pydantic import BaseModel


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
