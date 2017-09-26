# Nash equilibrium computation
# Ian Bishop
# 2017-9-26

# computes Nash Equilibrium
def Nash():
    # sort users by cost
    users = [] # k
    num_users = 0 # n
    users.sort()
    reward = 0 # R

    # select the users
    selected_users = [0,1] # S
    i = 2
    total_selected_cost = 0 # sum(j in S, kj)
    total_selected_cost += selected_users[0] + selected_users[1]
    while i < num_users and users[i] < (users[i] + total_selected_cost) / len(selected_users):
        selected_users.append(users[i])
        total_selected_cost += selected_users[i]
        i += 1
    
    # calculate the optimal strategy for each user
    tne = [] # sensing time strategy
    for i in range(num_users):
        tne.append(0)
        if selected_users.count(i)>0:
            tne[i] = ((len(selected_users)-1) * reward / total_selected_cost) * (1 - (len(selected_users)-1) * users[i] / total_selected_cost)
    return tne

t = Nash()
print(t)