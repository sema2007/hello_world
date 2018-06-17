# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 19:19:41 2018

@author: sema
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:50:19 2018

@author: sema
"""

import requests as r
import json

from time import time

start = time()



gg=r.get('https://auchan.ua/api/rest/auchan_stock/store/')
st=gg.json()
z=7
for jj in range(len(st['city'])):
    for ii in st['city'][jj]['markets']:
        store_id = str(ii['id'])
        z+=1
        print(ii['name'])
        
        j=0
        
        for i in ('04820123630092','04820123630115','auchan02207170000009','auchan02211452000007','00000040145853','00000040145037','04820023714076','auchan02207231000009','auchan02207232000008','04820034210437'):
            
            url= 'https://auchan.ua/api/barcode/{0}/user/sema2007@ukr.net/store/{1}'.format(str(int(i[-13:])),store_id)
            j+=1
            try:
                data= r.post(url).json()
                print(data['name']+ ": " + str(data['unit_price']/100) )
                
            except:
                next
                
        #wb.Save()

        
        print (ii['id'])
        print(time() - start)


