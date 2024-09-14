from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert

# Connect to the database
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Fetch all bands from the database
all_bands = session.query(Band).all()

# Print details for each band
for band in all_bands:
    print(f"Band: {band.name}")
    print(f"From: {band.hometown}")
    
    concerts = band.concerts  # Get all concerts for this band
    if concerts:
        for concert in concerts:
            venue = concert.venue
            print(f"Performed at: {venue.title} in {venue.city} on {concert.date}")
    else:
        print("No concerts found for this band.")
    
    print("-" * 40)  # Divider between bands

session.close()
