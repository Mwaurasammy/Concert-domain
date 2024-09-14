from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    
    concerts = relationship("Concert", back_populates="band")

    def get_concerts(self):
        return self.concerts

    def venues(self):
        return {concert.venue for concert in self.concerts}
    
    def play_in_venue(self, venue, date, session: Session):
        concert = Concert(band=self, venue=venue, date=date)
        session.add(concert)
        session.commit()

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]
    
    @classmethod
    def most_performances(cls, session: Session):
        return max(session.query(cls).all(), key=lambda band: len(band.concerts))

class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    
    concerts = relationship("Concert", back_populates="venue")
    
    def get_concerts(self):
        return self.concerts
    
    def bands(self):
        return {concert.band for concert in self.concerts}
    
    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)
    
    def most_frequent_band(self):
        band_concert_counts = {band: 0 for band in {concert.band for concert in self.concerts}}
        for concert in self.concerts:
            band_concert_counts[concert.band] += 1
        return max(band_concert_counts, key=band_concert_counts.get)

class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String, nullable=False)

    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")
    
    def get_band(self):
        return self.band
    
    def get_venue(self):
        return self.venue
    
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
