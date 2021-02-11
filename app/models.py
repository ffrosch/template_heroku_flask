from datetime import datetime

from sqlalchemy import func, ForeignKey, Column, Date, Integer, String, Time
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from app import db


class Testpoint(db.Model):
    """A tour/trip, including its geospatial data."""

    __tablename__ = 'testpoints'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    date = Column(Date, nullable=False)
    location = Column(Geometry(geometry_type="POINT", srid=4326), nullable=False)
