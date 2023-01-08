from sqlalchemy import select
from sqlalchemy.orm import Session

from ...db import TradeEntity, AssetEntity

def query_trades(session: Session, base_symbol: str) -> list[TradeEntity]:

    selector = select(TradeEntity)
    query = selector.join(AssetEntity, TradeEntity.base_id == AssetEntity.id_).where(AssetEntity.symbol == base_symbol)

    results = session.execute(query)
    return results.scalars().fetchall()
