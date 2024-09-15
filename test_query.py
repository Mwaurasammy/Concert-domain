# test_query.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert

# Connect to the database
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Fetch the first band
first_band = session.query(Band).first()
print(f"Band: {first_band.name}")
print(f"From: {first_band.hometown}")

# Print venues for the first band
print("\nVenues where the band has performed:")
for venue in first_band.venues():
    print(f"{venue.title} in {venue.city}")
print("-" * 40)

# Print concerts for the first band
print(f"Concerts for '{first_band.name}':")
for concert in first_band.get_concerts():
    print(f"Performed at: {concert.venue.title} in {concert.venue.city} on {concert.date}")
print("-" * 40)

# Fetch the first concert
first_concert = session.query(Concert).first()
print(f"Concert introduction for '{first_concert.band.name}' at {first_concert.venue.title}:")
print(first_concert.introduction())
print(f"Is it a hometown show? {'Yes' if first_concert.hometown_show() else 'No'}")
print("-" * 40)

# Fetch the first venue
first_venue = session.query(Venue).first()
print(f"Bands that performed at {first_venue.title}:")
for band in first_venue.bands():
    print(f"{band.name} from {band.hometown}")
print("-" * 40)

# Print all introductions for the first band
print(f"All introductions for '{first_band.name}':")
for intro in first_band.all_introductions():
    print(intro)
print("-" * 40)

# Test Band's play_in_venue method
new_venue = session.query(Venue).filter_by(title="The Carnivore Grounds").first()
first_band.play_in_venue(new_venue, "2024-12-31", session)
print(f"New concert added for '{first_band.name}' at {new_venue.title} on 2024-12-31")
print("-" * 40)

# Test Venue's concert_on method
concert_on_date = first_venue.concert_on("2024-09-14")
if concert_on_date:
    print(f"Concert on 2024-09-14 at {first_venue.title} by {concert_on_date.band.name}")
else:
    print(f"No concert on 2024-09-14 at {first_venue.title}")
print("-" * 40)

# Test Band.most_performances() method
most_active_band = Band.most_performances(session)
print(f"The band with the most performances is: {most_active_band.name}")
print("-" * 40)

# Test Venue.most_frequent_band() method
most_frequent_band = first_venue.most_frequent_band()
print(f"The band that performed the most at {first_venue.title} is: {most_frequent_band.name}")
print("-" * 40)

session.close()
