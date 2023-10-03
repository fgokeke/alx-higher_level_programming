Tasks
0. Who am I?
mandatory
What function would you use to get the type of an object?

Write the name of the function in the file, without ().

1. Where are you?
mandatory
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. Right count
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

3. Right count =
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

4. Right count =
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

5. Right count =+
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

6. Is equal
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

7. Is the same
mandatory
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

8. Is really equal
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

9. Is really the same
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

10. And with a list, is it equal
mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

11. And with a list, is it the same
mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

12. And with a list, is it really equal
mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

13. And with a list, is it really the same
mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

14. List append
mandatory
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

15. List add
mandatory
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

16. Integer incrementation
mandatory
What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

17. List incrementation
mandatory
What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
