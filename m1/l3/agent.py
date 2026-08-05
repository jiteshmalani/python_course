name=input("what is your name? ")
gajet=input("whats your favourate gajet? ")
agent_number=input("what is your agent number? ")

is_active=True
print(type(name))
print(type(gajet))
print(type(agent_number))
print(type(is_active))
agent_number=int(agent_number)
print(type(agent_number))
a=name[0:2]
b=name[-2: ]
agent_badge=a+b+str(agent_number)
print(agent_badge)