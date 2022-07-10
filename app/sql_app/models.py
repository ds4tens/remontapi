from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

import enum

class OrderStatus(enum.Enum):
    created = "created" # заказ создан
    pending = "pending" # ожидает назначения мастера
    awaiting = "awaiting" # мастер в пути
    processing = "processing" # заказ выполняется
    submitted = "submitted" # заказ выполнен

Base = declarative_base()

class Order(Base):
    __tablename__ = "Order"
    id = Column(Integer, primary_key=True)
    сustomer_name = Column(String)
    customer_address = Column(String)
    addr_cords = Column(String) # координаты формата (x. ; y.)
    status = Column(Enum(OrderStatus))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_update = Column(DateTime(timezone=True), onupdate=func.now())
    