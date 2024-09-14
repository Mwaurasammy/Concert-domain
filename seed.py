from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert, Base

engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Clear the existing records to prevent duplicates
session.query(Concert).delete()
session.query(Band).delete()
session.query(Venue).delete()

# Create Bands
band1 = Band(name="The Rolling Stones", hometown="London")
band2 = Band(name="Sauti Sol", hometown="Nairobi")
band3 = Band(name="Of Monsters and Men", hometown="Iceland")
band4 = Band(name="Nirvana", hometown="Washington")

# Create Venues
venue1 = Venue(title="Madison Square Garden", city="New York")
venue2 = Venue(title="The Carnivore Grounds", city="Nairobi")
venue3 = Venue(title="Wembley Stadium", city="London")
venue4 = Venue(title="Super Bowl", city="Las Vegas")

# Create Concerts (multiple concerts for same band at different venues)
concert1 = Concert(band=band1, venue=venue1, date="2024-09-14")  # Rolling Stones at Madison Square Garden
concert2 = Concert(band=band1, venue=venue3, date="2024-10-10")  # Rolling Stones at Wembley Stadium
concert3 = Concert(band=band2, venue=venue2, date="2024-09-20")  # Sauti Sol at The Carnivore Grounds
concert4 = Concert(band=band2, venue=venue4, date="2024-11-15")  # Sauti Sol at Super Bowl
concert5 = Concert(band=band3, venue=venue3, date="2024-10-05")  # Of Monsters and Men at Wembley Stadium
concert6 = Concert(band=band4, venue=venue4, date="2024-11-11")  # Nirvana at Super Bowl

# Same band performing at the same venue on different dates
concert7 = Concert(band=band1, venue=venue1, date="2024-12-01")  # Rolling Stones at Madison Square Garden again
concert8 = Concert(band=band2, venue=venue2, date="2024-12-10")  # Sauti Sol at The Carnivore Grounds again

# Add everything to the session
session.add_all([band1, band2, band3, band4, venue1, venue2, venue3, venue4, 
                 concert1, concert2, concert3, concert4, concert5, concert6, concert7, concert8])

session.commit()
