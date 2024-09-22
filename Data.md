# 1. String 
`String` are sequences of characters, using the syntax of either single quotes or double quotes:
```python
'hello'
"hello"
```
These actions use `[]` and number index to indicate positions of what you wish to grab.

Slicing allows you to grab a subsection of multiple characters.
```python
string[start:stop:step]
```
## Properties and Methods
* **Immutability** : Don't change any characters in string.

## Print format with String
Let's explore two methods for this:
* `.format()` method
* `f-strings`
```bash
print('This is a string {}'.format('INTERTED'))
print('The {0} {1} {2}'.format('fox','brown','quick'))
print('The result was {:10.3f}'.format(r))
```
```bash
print(f'Hello, my name is {name}')
```
# 2. List
`List` are ordered sequences that can hold a variety of object types.

They use `[]` and commas to separate object.
```bash
[1,2,3,4,5]
```
List support indexing and slicing.

## Basic List Methods
Use the `append` to add an item to the end of a list
```bash
list.append('anything')
```
Use `pop` to 'pop off' an item. By default pop takes off the last index, but you can also specify which index to pop off.
```bash
# Pop off the 0 indexed item
list.pop(`)
```
We can `sort` and `reverse` methods to also effect your list.

## Nesting Lists 
```bash
lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]
matrix = [lst_1,lst_2,lst_3]
# output: matrix = [[1,2,3],[4,5,6],[7,8,9]]
```
# 3. Dictionaries
A Python `dictionary` consists of a key and the an associated value. That value can be almost any Python object.
## Constructing a Dictionary
```bash
# Make a dictionary with {}
my_dict = {'key1': 'value1', 'key2':[0,1,2]}
# Call values by their key
my_dict['key1']
# Can call an index on that value
my_dict['key2'][0]
```
We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it.
```bash
# Create a new dict
d = {}
# Create a new key through assignment
d['animal'] = 'dog'
d['answer'] = 123
# output: d = {'animal': 'dog, 'answer': 123}
```
```bash
# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1': {'nestkey': {'subnestkey': 'value'}}}
# Keep calling the keys
d['key1']['nestkey']['subnestkey']
```
## A few Dictionary Methods
```bash
d = {'key1': 1, 'key2': 2, 'key3': 3}
# To return a list of all keys
d.keys() # dict_keys(['key1', 'key2'])
# To grab all values
d.values() # dict_values([1,2])
# To return tuples of all items
d.items() # dict_items([('key1', 1),('key2'),2])
```

# 4. Tuples
Tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed. You should use tuples to present things that shouldn't be changed, such as days of the weeks, or dates on a calendar.
## Constructing Tuples
```bash
t = ('one',2)
```
## Basic Tuple Methods
```bash
# To enter a value and return the index
t.index('one') #0
# To count the number of times a value appears
t.count('one') #1
```

# 5. Sets
Sets are unordered collection of unique elements. We can construct them by using the set() function.
```bash
x = set()
# We add to sets with a add() 
x.add(1) # x = {1}
```
Notice how it won't place another 1 there.
```bash
list = [1,1,1,1,2,3,3,4,5,5]
set(list) # {1,2,3,4,5}
```
