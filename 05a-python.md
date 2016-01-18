# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both tuples and lists are objects that contain however many elements the user likes. They both are ordered, with indexes for each element. Tuples, however, are immutable, meaning their values cannot be changed once assigned. Lists can be changed after being set initially. For this reason, only tuples work in dictionaries, as keys cannot be mutable in python.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both objects that contain multiple elements. Lists are ordered, and sets are not. Lists can contain duplicate elements, while sets cannot. Elements in sets must be immutable, while elements in lists don't have to be. A set could be used to identify the different products sold at a store on a given day. A list could be used to identify the order of the products sold, as well as the number of each product sold. Finding an element in a set is considerably faster than finding an element in a list, because sets, being immutable, use a hash function to essentially resize the data contained, making it faster. To find an element in a list, python must iterate through each element until it finds it.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is one of two ways to create a function in Python (the other being 'def'). It creates a function without naming it, using an abbreviated syntax to take up less lines of code. It can only return a single value. It lacks functionality compared to 'def' but is useful to create more streamlined code.


box_dimensions = [
  ('a', 5, 8, 12),
  ('b', 7, 9, 8),
  ('c', 10, 6, 9)
]  #create list (of tuples) to sort

sorted(box_dimensions, key = lambda box: box[1]) # sort by length

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





