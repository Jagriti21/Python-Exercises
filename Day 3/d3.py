#Given a list of tuples with current and min balances:
#[("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)] 
# use comprehensions to get the below:
l = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
print(l)

#dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}
d = dict((idx[0], idx[1]) for idx in l if idx[1]>=idx[2])
print(d)

#set of all balances {2000, -52, 900}
s = {bal[1] for bal in l}
print(s)

#list of account holders ["Guido", "Raymond", "Jack", "Brandon"]
l1 = [nam[0] for nam in l]
print(l1)

#dict of user and money each need to fulfill the min balance requirement 
#(those who already have enough bal should not be in the dict) {"Raymond": 1052, "Jack": 100}
d1 = dict((i[0],(i[2]-i[1])) for i in l if (i[1]-i[2])<i[2])
print(d1)

#list of tuples with name and current balance if the balance is above 0 [("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]
lt = [(i[0],i[1]) for i in l if i[1]>0]
print(lt)