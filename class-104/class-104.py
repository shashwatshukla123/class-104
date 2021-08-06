#descriptive statistic mean , median, mode etx describe sometime  
#descriptive data is the data which give us some infomation
#statistic means colloction of data 
#
#mean: (average)=sum of values / the number of values
#
#median: arrange the data in sorted order then find the middle value.
#if there are 2 middle find their mean, that is the median
#for ever number of data there are 2 middle and for odd number there is 1 middle number.
#
#mode: used to find the most occuring value of a dataset.
#
#python has a colloction module which has a counter method it is a container which counts how many times the same values are reppeated#

from collections import Counter
new_data="whitehatjr"
data=Counter(new_data)
print(data)

new_list=data.items()
print(new_list)

#print(dictionary.items())
# dictionary.items():- is used to return the list with all dictionary keys with values
value=data.values()
print(value)