#!/usr/bin/env python
# coding: utf-8

# In[10]:


# create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
print(st)
for elm in st.split() :
    if elm[0] == 's':
        print(elm)


# In[13]:


# print all the even numbers from 0 to 10
for num in range(0,10):
   if num%2 == 0:
        print(num)
        


# In[20]:


#create a list of all numbers between 1 and 50 that are divisible by 3
myDiv3List = []
for num in range(1,50):
    if num%3 == 0:
        myDiv3List.append(num)
        print(num)    


# In[25]:


#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for elem in st.split():
    if (len(elem) % 2 == 0):
        print("Word {0} has even length".format(elem))
    else:
        print("Word {0} has Odd length".format(elem))


# In[30]:


# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

for elem in range(1,100):
    if elem % 5 == 0 and elem % 3 == 0:
        print("Element {0} belongs to FizzBuzz".format(elem))
    elif elem % 3 == 0:
          print("Element {0} belongs to Fizz".format(elem))
    elif elem % 5 == 0:
          print("Element {0} belongs to Buzz".format(elem))
            


# In[36]:


#Create a list of the first letters of every word in the string below
st = 'Create a list of the first letters of every word in this string'
firstLetterList = []
for elem in st.split():
    firstLetterList.append(elem[0])
    
print(len(firstLetterList))
    


# In[ ]:
print(bin(10))



