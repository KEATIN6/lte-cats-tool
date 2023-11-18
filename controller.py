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
    
def check_range(test_range, category_range) -> bool:
    test_low, test_high = test_range
    category_low, category_high = category_range
    if int(category_low) < int(test_high) \
        and int(category_high) > int(test_low):
            return True
    return False
    
def get_available_categories(low, high):
    categories = get_all_categories()
    print([c.ul_low for c in categories])
    print([c.ul_high for c in categories])
    for category in categories:
        if check_range((low, high), (category.ul_low, category.ul_high)) \
            and check_range((low, high), (category.dl_low, category.dl_high)):
                print(category)
            
            
            
        
get_available_categories(850, 900)
    