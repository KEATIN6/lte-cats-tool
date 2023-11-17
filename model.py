# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:09:07 2023

@author: pizzacoin
"""

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

# %%

class LTECategoryOlv:
    def __init__(self, category, ul_low, ul_high, dl_low, dl_high, mode):
        self.category = category
        self.ul_low = ul_low
        self.ul_high = ul_high
        self.dl_low = dl_low
        self.dl_high = dl_high
        self.mode = mode

# %%

engine = create_engine("sqlite:///NetworkingDB.db", echo=True)
Base = declarative_base()
metadata = Base.metadata

# %%

class LTECategory(Base):
    __tablename__ = "LTECategories"
    
    Category = Column(Integer, primary_key=True)
    UplinkLow = Column(Integer)
    UplinkHigh = Column(Integer)
    
    DownlinkLow = Column(Integer)
    DownlinkHigh = Column(Integer)
    Mode = Column(String)
    
    def __init__(self, data=None):
        if isinstance(data, LTECategoryOlv):
            self.Category = data.category
            self.UplinkLow = data.ul_low
            self.UplinkHigh = data.ul_high
            self.DownlinkLow = data.dl_low
            self.DownlinkHigh = data.dl_high
            self.Mode = data.mode 
            
    def export(self):
        return LTECategoryOlv(
            self.Category, self.UplinkLow, self.UplinkHigh,
            self.DownlinkLow, self.DownlinkHigh, self.Mode
        )
            
# %%

Base.metadata.create_all(engine)

# %%