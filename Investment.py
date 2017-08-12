# -*- coding: utf-8 -*-

"""
Investment 
Created on 2017/06
@author: Tommy Xu
@contact: i@xht97.cn
"""

import tushare as ts
import pandas as pd
from urllib import request
import numpy as np
# import sklearn
# import matplotlib
import datetime
import math
import os

class Portfolio:
    """
    A class which you can quickly complete your investment homework with.
    """   
    stocklist = []
    ratio = []
    moneyallocation = []
    baseearning = 0
    start = None
    end = None
    
    stockdata = pd.DataFrame()
    defaultpath = './'
    
    def __init__(self, stock_list, ratio_input, start_input, end_input):
        """
        Initialize with parameters you input.When using the class, you should instantiate this class.
        You need to input at least the stock_list data to ensure the program's running.
        parameters:
        -----
        stock_list: string list
        ratio_input: float number list
        start_input: string, example: 2017-08-10
        end_input: string, example: 2017-08-12
        """
        self.stocklist = stock_list
        self.ratio = ratio_input
        self.start = start_input
        self.end = end_input
        # Check if the length of stocklist and ratio are the same
        if len(self.stocklist) == len(self.ratio):
            pass
        else:
            print("There exists an error with the list and ratio!")
    
    def allocate(self, money_of_investment):
        """
        Input the total amount of money and allocate it with the ratio which has been input or calculated by the program.
        """
        moneyalloction = []
        if self.stocklist == []:
            print("There is no protfolio in memory!")
        for i in range(0, len(self.ratio)):
            moneyalloction.append(self.ratio[i] * money_of_investment)
        self.moneyallocation = moneyalloction
        
    def set_default_path(self, path_input):
        """
        Set default path of class.
        """
        self.defaultpath = path_input
        
            
    def set_base_earning(self, excess_earning):
        """
        Set you base earning so the program can get you excess earning.
        """
        self.baseearning = excess_earning
    
    def index_model(self):
        """
        Build a asset protfolio using index model.
        """
        hs300_data = ts.get_hist_data('hs300', self.start, self.end)
        self.stockdata['hs300'] = hs300_data['close']
        for stock_single in self.stocklist:
            self.stockdata[stock_single] = ts.get_hist_data(stock_single, self.start, self.end)['close']
        returns = (self.stockdata/self.stockdata.shift(1))-1
        
        
        
        
        
        print('This function will be completed later!')
        
        # To be continued
        
    def markowitz_model(self):
        """
        Build a asset protfolio using Markowitz model.
        """
        print('This function will be completed later!')
            
    def data_to_csv(self, path_input):
        """
        Output the data of your asset portfolio with the format '.csv' to the place you want.
        """
        try:
            for i in range(len(self.stocklist)):
                self.stockdata[self.stocklist[i]]
        except:
            hs300_data = ts.get_hist_data('hs300', self.start, self.end)
            self.stockdata['hs300'] = hs300_data['close']
            for stock_single in self.stocklist:
                self.stockdata[stock_single] = ts.get_hist_data(stock_single, self.start, self.end)['close']             
        data = self.stockdata
        data.to_csv(path_input+'data.csv')
        print("The file has been generated at ", path_input, ".")
        
    def profile(self, path_input=None):
        """
        Calculate the profile made by your portfolio. It will give out the number of money you made, instead of pecentage.
        """
        profile = []
        profileratio = []
        sum_of_profile = 0
        for stock_single in self.stocklist:
            print("Now processing:", stock_single)
            self.stockdata[stock_single] = ts.get_hist_data(stock_single, self.start, self.end)['close']
            profileratio.append((self.stockdata[stock_single].loc[self.end]-self.stockdata[stock_single].loc[self.start])/self.stockdata[stock_single].loc[self.start])
        for i in range(0, len(self.stocklist)):
            profile.append(self.moneyallocation[i] * float(profileratio[i]))
            if math.isnan(profile[i]) != True:
                sum_of_profile = profile[i] + sum_of_profile
            else:
                pass
        for i in range(0, len(profile)):
            print(self.stocklist[i], profile[i],"\n")
        print("Totel profile is", sum_of_profile)
        # Update: 2017-08-12
        try:
            if path_input != None:
                _profile_stock_list = self.stocklist.append('Totel profile')
                _profile_single_stock = profile.append(sum_of_profile)
                _profile_data = {'List':_profile_stock_list, 'Profile':_profile_stock_list}
                _profile = pd.DataFrame(_profile_data)
                _profile.to_csv(path_input+'profile.csv')
            elif self.defaultpath:
                _profile_stock_list = self.stocklist.append('Totel profile')
                _profile_single_stock = profile.append(sum_of_profile)
                _profile_data = {'List':_profile_stock_list, 'Profile':_profile_stock_list}
                _profile = pd.DataFrame(_profile_data)
                _profile.to_csv(self.defaultpath+'profile.csv')
            else:
                pass
        except IOError:
            print('Path not exists!')
        
    def get_graph(self, stock_code, option=1, path_input):
        """
        Using sina's finance API to get the graph of the stocks.You need to provied stock_code and option at least
        to ensure this function's running.
        """
        # Example URL of Sina's API
        # http://image.sinajs.cn/newchart/daily/n/sh601006.gif
        # http://image.sinajs.cn/newchart/min/n/sh000001.gif        
        header ={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
        }
        
        if stock_code[0] == '6':
            stock_code = 'sh' + stock_code
        else:
            stock_code = 'sz' + stock_code
        # 1 means getting K-Graph; 2 means getting Timming-Graph
        try:
            if option == 1:
                graph = request.urlopen('http://image.sinajs.cn/newchart/daily/n/'+stock_code+'.gif', data = header)
            if option == 2:    
                graph = request.urlopen('http://image.sinajs.cn/newchart/min/n/'+stock_code+'.gif', data = header)
            with open(path_input+stock_code+'.gif', 'wb') as file:
                file.write(graph)
            print('Graph generated!')
        except Exception as e:
            print(e)
            
                
if __name__ == '__main__':
    Portfolio.__init__()