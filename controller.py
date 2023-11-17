# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:32:23 2023

@author: pizzacoin
"""

from model import LTECategory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect_to_database():
    engine = create_engine("sqlite:///NetworkingDB.db", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def get_all_categories():
    session = connect_to_database()
    results = session.query(LTECategory).all()
    return [result.export() for result in results]
    


def get_available_categories(uplink, downlink):
    categories = get_all_categories()
    print([c.ul_low for c in categories])
    for category in categories:
        if int(category.ul_low) <= int(uplink):
            print(1)
            if category.ul_high > uplink:
                print(2)
                if category.dl_low <= downlink:
                    print(3)
                    if category.dl_high > downlink:
                        print(category)
        
        
get_available_categories(1800, 1900)
    