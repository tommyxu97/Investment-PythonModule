# -*- coding: utf-8 -


import Investment as iv

# gupiaolist = ['000048','000601','000561','002618','300003','002168','002134','002389','600809','600132','600429','000651','000333','002050','000921','600690','600267','600211','002294','300026','600535','300014']
# gupiaoratio = [0.0424,0.0410,0.0621,0.0424,0.0428,0.0600,0.0320,0.0350,0.052,0.0362,0.023,0.0603,0.0618,0.0404,0.0625,0.0408,0.0406,0.022,0.041,0.0592,0.042,0.0615]

# gupiaolist = ['600519','000651','600004','600056','000027','600275','600211','600138','600338']
# gupiaoratio = [0.01475727,-0.1634576,0.0909141,-0.1482347,-0.2408261,0.00301813,-0.0358125,0.04453949,-0.1370716]

# gupiaolist = ['600211','600900','000662','000070','600119','000538','000615','600816','002078','601818','002043','600312','600785']
# gupiaoratio = [0.0053833,0.0268534,-0.005876,-0.000193,0.00366666,0.0253908,0.0091932,0.0265484,0.0115391,0.013637,0.0161995,0.001777,-0.01707]

gupiaolist = ['000796','002185','601880','601939','600463','000910','600391','600119','600446','300226','000028','000001']
gupiaoratio = [0.091,0.1387,0.0921,0.2153,0.1746,0.1637,0.1061,0.1385,0.0869,0.0679,0.2161,-0.4909]
 
start = '2017-04-21'
end = '2017-06-15'

gupiao = iv.Portfolio(gupiaolist, gupiaoratio, start, end)
gupiao.allocate(1000)
gupiao.profile()

gupiao.data_to_csv("./data.csv")


# gupiao.getGraph('000796', 1, "../data.png")
