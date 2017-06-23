# Investment-Python Module

>A Python Module which helps you deal with your investment homework with ease. You can use this module to build your asset portfolio by index model or Markowitz model.

## Setup

Now the code has not been uploaded to pip. So please download it and add to your project. Later you can get it easier with pip:

	# pip install investment

## Dependence

>This module is developed under Python 3.6.1, so it may not work with Python 2.X.

The four modules that mainly used in Investment are:

- Tushare
- Pandas
- Numpy
- Matplotlib(Till now this module isn't being used)

## Usage

### Import

Import this module with the following code in your python file:

	import investment as iv

### func \_\_init__()

If you want use this module, the very first thing you should do is to initialize a object with function \_\_init__. 
You can do this with the following code:

	stock_list = []
	ratio_input = []
	start_input = '2017-05-01'
	end_input = '2017-06-15'
	stock_model = iv.assetPortfolio(stock_list, ratio_input, start_input, end_input)
	
*Note: stock_input is a string list of stock code, you can input it like this: ['000001', '600237']; ratio_input is a float list like [0.25, 0.21]. start_input (and end_input) is a str varible like '2017-05-23'*

### func allocate()

Allocate money to your portfolio(It will allocate by the ratio you input or that generated by the model in this module):

	stock_model.allocate(total_money_input)

### func profile()

Get the profile by your portfolio:

	stock_model.profile()

*Note: The profile given by the program won't be the percentage.*

>Documents of other functions will be added.

## Author

TommyXu

[HomeSite](xht97.cn)
[Blog](blog.xht97.cn)

[Email:i@xht97.cn](tomail:i@xht97.cn)

<<<<<<< HEAD
![logo](logo.ico)
=======
![logo](http://cdn.xht97.cn/logo.png)
>>>>>>> 06e469ecc24e79aab3b0e0ed334df98cf725b3b2



