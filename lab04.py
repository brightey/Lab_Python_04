groceries= ['bananas','strawberries','apples','bread']

#a
#ADDING CHAMPAGNE TO THE LIST'S END

groceries.append('champagne')
print groceries

#removing bread
groceries.remove('bread')
print groceries



#2 THE DICTITIONARY
store={'Apples':'SPIC_APPLES',
       'Bananas':'SPIC_BANANAS',
       'Bread':'SPIC_BREAD'
       ,'Carrots':'SPIC_CARROTS',
       'Champagne':'SPIC_CHAMPAGNE',
       'Strawberries':'SPIC_STRAWBERRIES'}
print 'the price for apples is : ', store['Apples']

#changing the price of strawberries
del store['Strawberries']
store['Strawberries']='WPIC_STRAWBERRIES'
print store

#ADDING CHICKEN TO THE LIST
store['Chicken']='SPIC_CHICKEN'
print store

#3 the tuples
stock=('APPLES','BANANAS','BREAD','CARROTS','CHAMPAGNE','STRAWBERRIES')
print' printing the tuples', stock


#4 creating the function
PriceList=['$0.50', '$1.25', '$1.50','$0.2']

x=raw_input("enter a price list you want to add :")

#def func(x):
 PriceList=['$'+'0.50', '$'+'1.25', '$'+'1.50' ,'$'+'0.2','$'+x]
print PriceList
 
    

