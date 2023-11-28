def hello_name(user_name):
    print("hello_" + user_name)
    
def first_odds():
    lst = list(range(1,101))
    for i in lst:
        if i % 2 == 0:
            pass
        else:
            print(i)   

def max_num_in_list(a_list):
    max_v = max(a_list)
    return max_v

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0 or a_year % 400 == 0:
            return True
    else:
        return False
    
def is_consecutive(a_list):
    return a_list == list(range(min(a_list), max(a_list)+1))
    
#driver oode
user_name = "Anas"
hello_name(user_name)
first_odds()
a_list = [1, 4, 1000, 9, 95]
print(max_num_in_list(a_list))
a_year = 2004
print(is_leap_year(a_year))
a_year = 1999
print(is_leap_year(a_year))
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [2,3,4,6,7,5]
print(is_consecutive(a_list))





