# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 8:03:45 2021

@author: Bhaumik
"""
import math
import os

def coinCalculation2(val):
    if (val == 0):
        return 'Empty String'
    
    cDefault = [200,100,50,20,10,5,2,1]
    coinArray = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(len(cDefault)):
       coinArray[i] = val//cDefault[i]
       val = val % cDefault[i]
    return coinArray
"""      
def coinCalculate(val):
   cDefault = [200,100,50,20,10,5,2,1]
   coinArray = [0, 0, 0, 0, 0, 0, 0, 0]
   
   coinArray[0] =  val//200
   val = val % 200

   coinArray[1] = val//100
   val = val % 100
   
   coinArray[2] = val//50
   val = val % 50
   
   coinArray[3] = val//20
   val = val % 20
   
   coinArray[4] = val//10
   val = val % 10
   
   coinArray[5] = val//5
   val = val % 5
   
   coinArray[6] = val//2
   val = val % 2
   
   coinArray[7] = val//1
   val = val % 1
   
   return coinArray
   
   #if (val == 0):
   #    return 0
    
#cDefault = [200,100,50,20,10,5,2,1]
"""
def simplifyCheck(val):
    
    ###############Abnormal string check####################
    #checking empty string
    if len(val) == 0:
        return 'Error String Empty'
    #checking abnormals
    temp = val.replace('.','')
    temp = temp.replace('£','')
    temp = temp.replace('p','')
   
    if  any(i.isalpha() for i in temp):
        #print('aplhanumeric error')
        return 'Error Non-numeric, non-symbol character'
    
    if len(temp) == 0:
        return 'Error no number'
    #print(temp)
    
    
    #################### Normalizing the input ####################
    
    #if input cotains only number which doesn't need further conversion 
    #example 12, 154, 56, 98
    if val.isdecimal():
        #print('from deci')
        return str(val)
    
    
    ### if input contains only number with p(penny) character or 
    ### it is a string which has p(penny) charcter
    ### example 123p 12p 334p
    if 'p' in val:
       val = val.replace('p','')
       if val.isdecimal():
           #print('from deci p')
           return str(val)
    
    
    
    ## If input contains pound £ symbol which leads to multiplication of numbers by 100
    ## If string contains '.' symbol which needs to be evaluated
    if '£' in val or '.' in val:
        val = val.replace('£','')
        #print(val)
        
        deci =  val.split('.')
        if len(deci) > 1:
            if len(deci[1]) > 2:
                val = round(float(val),2)
                
        val = float(val)*100
        #print('from £ and/or .')
        return str(val)
        
    
if __name__ == "__main__":
    value = input("Enter value: ")
    os.system('cls')
    print('\n'*10)
    val = value
    ans = simplifyCheck(val)
    #print(ans)
    e = 'Error'
    if  ans.find(e) == -1:
        #fAns = coinCalculate(ans)
        #print(fAns)
        #print('init')
        ans = float(ans)
        fAns2 =  coinCalculation2(ans)
        #print(fAns2)
        print('=======================')
        print('Coin Denominations for ')
        print('      '+value)
        print('=======================')
        print('£2   x  '+str(math.trunc(fAns2[0])) + ' Coins')
        print('£1   x  '+str(math.trunc(fAns2[1])) + ' Coins')
        print('50p  x  '+str(math.trunc(fAns2[2])) + ' Coins')
        print('20p  x  '+str(math.trunc(fAns2[3])) + ' Coins')
        print('10p  x  '+str(math.trunc(fAns2[4])) + ' Coins')
        print(' 5p  x  '+str(math.trunc(fAns2[5])) + ' Coins')
        print(' 2p  x  '+str(math.trunc(fAns2[6])) + ' Coins')
        print(' 1p  x  '+str(math.trunc(fAns2[7])) + ' Coins')
        print('=======================')
        
    else:
        print(ans)