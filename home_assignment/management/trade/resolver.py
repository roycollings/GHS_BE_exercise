import uuid
import strawberry
from decimal import Decimal

from ...deps import GenieInfo
from ..asset.resolver import Asset
from ..scalars import ArrowType
from .database import query_trades

@strawberry.type
class Fee:
    currency_id: str
    currency: Asset
    amount: Decimal

@strawberry.type
class LabelKey:
    name: str

@strawberry.type
class UserType:
    username: str

@strawberry.type
class LabelValue:
    key_id: str
    key: LabelKey
    value: str
    trade_id: uuid.UUID

@strawberry.type
class Trade:
    base_id: str
    base: Asset

    quote_id: str
    quote: Asset

    fee_id: str
    fee: Fee

    user_id: str
    user: UserType

    labels: list[LabelValue]

    amount: Decimal
    price: Decimal
    placed_at: ArrowType

@strawberry.input
class BaseFilter:
    base_symbol: str

@strawberry.input
class PageFilter:
    number: int
    size: int

@strawberry.type
class ReturnValue:
    total_count: int
    trades: list[Trade]

async def get_trades(info: GenieInfo, filter: BaseFilter, page: PageFilter) -> ReturnValue:
    start = (page.number - 1) * page.size
    stop = start + page.size

    with info.context.session_factory.begin() as session:
        total_trades = query_trades(session, filter.base_symbol)
        trades_for_page = total_trades[start:stop]

        return ReturnValue(
            total_count=len(total_trades),
            trades=[Trade(
            base_id=trade.base_id,
            base=trade.base,

            quote_id=trade.quote_id,
            quote=trade.quote,
            
            fee_id=trade.fee_id,
            fee=trade.fee,

            user_id=trade.user_id,
            user=trade.user,

            labels=trade.labels,

            amount=trade.amount,
            price=trade.price,
            placed_at=trade.placed_at,
            ) for trade in trades_for_page]
        )
