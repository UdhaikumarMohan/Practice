data = {1:'Udhai', 2:'Pavithra', 3:'Madhan', 4:'Akhila'}

if data[1]=="Udhai":

    print("yes")

for a in data:
    print(a)
data.items()
data
#Specify the keys to fetch values
data[2]
data.keys()
data.values()
data["Udhai"]

for x, y in data.items():

    print (x, y)

data.get(1)
print(data.get(0))
print(data.get(1, 'Not found'))
print(data.get(5, 'Not found'))

# You can use string to tell about non exsisting data.

# Creating dictionaries using two lists.

Keys = ["Udhai", "Pavithra", "Madhan", "Akhila"]
Values = ["Loves Python", "Loves Research", "Loves Eating", "Loves Music"]

data = dict (zip(Keys, Values))
data

#Add new value:

data['Udhai']
data['Rubina']
data['Rubina'] = "Loves Makeup"
data

# Delete valus in dictionary

del (data["Rubina"])
data

# To fetch items
data.items()
new=data.copy()
new

# To update values
data.update({"Akhila":"Loves Music and Dance"})

# This another method to add value to dictionary, if the key you typing dosen't exists means.
# It will automatically update the value you wants. If the key alreay exists, given value does't change.
# If key does'nt exists it include that key and the default value. If you not give value
# Then it adds that key and give value none
data.setdefault("Varun", "Loves to work in Singapore")
data.update({"Varun":"Loves Singapore"})
data.setdefault("Iniyan")
data


x_key = ('key1', 'key2', 'key3')
y_value = 0

new_Dict = dict.fromkeys(x_key, y_value)
new_Dict





