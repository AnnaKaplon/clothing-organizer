from enum import Enum

from sqlalchemy import Column, Integer, String, Enum as SAEnum

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
    name = Column(String, required=True)
    clothing_type = Column(SAEnum(ClothingType), required=True)
    color = Column(SAEnum(Color), required=True)
