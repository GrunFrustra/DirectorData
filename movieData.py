# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 22:44:33 2019

@author: ryang
"""
import re
#director = moviebs.find('meta',{'name': 'twitter:data1'})
class movieData():
    def __init__(self, bs):
        self.runtime = bs.find('p',{'class': 'text-link text-footer'}).text.strip().replace('\xa0', ' ')
        pattern = re.compile('^.*mins')
        self.runtime = pattern.findall(self.runtime)
        
        self.watches = bs.find('li',{'class': 'stat filmstat-watches'})
        self.watches = self.watches.find('a')['title']
        pattern2 = re.compile('[0-9^,]+')
        self.watches = pattern2.findall(self.watches)
        
        #<meta name="twitter:label2" content="Average rating" /><meta name="twitter:data2" content="3.93 out of 5" />
        self.rating = bs.find('meta',{'name': 'twitter:data2'})
        self.rating = self.rating['content']
        pattern3 = re.compile('\d\.\d+')
        self.rating = pattern3.findall(self.rating)