
#!/usr/bin/env python
# coding: utf-8

# ## 2160. Minimum Sum of Four Digit Number After Splitting Digits

# In[16]:


def minimum_sum_of_four_digit_number(number):
    digits = sorted(str(number))
    return sum(int(digit) for digit in digits)

number = 2160
print(minimum_sum_of_four_digit_number(number))


# ## 1773. Count Items Matching a Rule

# In[2]:


def count_items(items, ruleKey, ruleValue):
    count = 0

    for item in items:
        if ruleKey == "type" and item[0] == ruleValue:
            count += 1
        elif ruleKey == "color" and item[1] == ruleValue:
            count += 1
        elif ruleKey == "name" and item[2] == ruleValue:
            count += 1

    return count


items = [
    ["phone", "blue", "pixel"],
    ["laptop", "silver", "macbook"],
    ["phone", "black", "iphone"],
    ["tablet", "blue", "ipad"],
    ["laptop", "black", "thinkpad"]
]
ruleKey = "color"
ruleValue = "blue"

item_count = count_items(items, ruleKey, ruleValue)
print("Number of items matching the rule:", item_count)


# ## 2351. First Letter to Appear Twice

# In[9]:


def first_letter_to_appear_twice(string):
    for letter in string:
        if string.count(letter) > 1:
            return letter
    return None


string = "2351"
first_double_letter = first_letter_to_appear_twice(string)
if first_double_letter:
    print("The first letter to appear twice:", first_double_letter)
else:
    print("The first letter to appear twice: l.")


# ## 1979. Find Greatest Common Divisor of Array

# In[4]:


import math

def find_gcd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = math.gcd(result, arr[i])
    return result


array = [19, 7, 9]
gcd = find_gcd(array)
print("Greatest Common Divisor:", gcd)


# In[ ]:




