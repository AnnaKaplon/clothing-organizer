from enum import Enum

from sqlalchemy import Column, Date, Integer, String, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import relationship

from organizer.models import Base


class ClothingType(Enum):
    accessories = "accessories"
    cardigan = "cardigan"
    dress = "dress"
    pants = "pants"
    pyjamas = "pyjamas"
    shoes = "shoes"
    skirt = "skirt"
    sweater = "sweater"
    top = "top"
    tshirt = "tshirt"


class Color(Enum):
    blue = "blue"
    green = "green"
    red = "red"
    pink = "pink"
    yellow = "yellow"
    purple = "purple"
    white = "white"
    black = "black"
    grey = "grey"
    beige = "beige"
    brown = "brown"


class Clothing(Base):
    """Clothing model definition"""
    __tablename__ = "clothing"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String, nullable=False)
    clothing_type = Column(SAEnum(ClothingType), nullable=False)
    color = Column(SAEnum(Color), nullable=False)
    buy_date = Column(Date)
    picture_url = Column(String)
    wearings = relationship("Wearing")
    washings = relationship("Washing")


class Wearing(Base):
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    clothing_id = Column(Integer, ForeignKey("clothing.id"))


class Washing(Base):
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    clothing_id = Column(Integer, ForeignKey("clothing.id"))
