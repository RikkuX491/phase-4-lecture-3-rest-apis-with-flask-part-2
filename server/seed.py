#!/usr/bin/env python3

from app import app
from models import db, Hotel

with app.app_context():
    
    Hotel.query.delete()

    hotels = []
    hotels.append(Hotel(name="Marriott", year_built=2000))
    hotels.append(Hotel(name="Holiday Inn", year_built=2001))
    hotels.append(Hotel(name="Hampton Inn", year_built=2002))

    db.session.add_all(hotels)
    db.session.commit()
    print("🌱 Hotels successfully seeded! 🌱")
