#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2) the original code shows the usage of random list in detail. 
# It's friendly to beginners, you can cleaerly understand how to use the element of list.
# The method provided by ChatGPT is shorter.
# It combined some steps, which may be hard to understand at first.


# In[1]:


import numpy as np  # Import the numpy library for random number generation and other utilities

all_door_options = (1, 2, 3)  # A tuple representing the three doors
my_door_choice = 1  # Player's initial choice
i_won = 0  # Track how many times the player wins by switching doors
reps = 100000  # Number of how many times the game is played

for i in range(reps):  # Repeat the simulation
    secret_winning_door = np.random.choice(all_door_options)  # Record the case of randomly selected the winning door
    all_door_options_list = list(all_door_options)  # Convert the tuple to a list for easier manipulation
    
    # Remove the winning door to be not revealed
    all_door_options_list.remove(secret_winning_door)

    try:
        # Try to remove the player's door choice from the list
        all_door_options_list.remove(my_door_choice)
    except:
        pass  # If the player's door was already removed, skip removing it again

    # Now, one or two doors are left in the list. Randomly reveal a goat door
    goat_door_reveal = np.random.choice(all_door_options_list)
    all_door_options_list.remove(goat_door_reveal)  # Remove the revealed goat door from the list

    # If the player's door is not the winning door, add the winning door back to the list
    if secret_winning_door != my_door_choice:
        all_door_options_list.append(secret_winning_door)

    # At this point, the list contains exactly one door: either the player's initial choice (if it's the winning door)
    # or the winning door (if it's not the player's original choice). The player "switches" to the other door.
    my_door_choice = all_door_options_list[0]  # The player switches to the other remaining door

    # If the player's new door choice is the winning door, increment the win counter
    if my_door_choice == secret_winning_door:
        i_won += 1

# After all repetitions, calculate the probability of winning by switching doors
i_won/reps  # This gives the proportion of times the player won by switching


# In[2]:


# Markov Chains and Text Generation
from IPython.display import YouTubeVideo
YouTubeVideo('56mGTszb_iM', width = 550)


# In[ ]:


# https://chatgpt.com/share/66ecbdc9-93b0-800f-8387-e2b66e35d451


# In[ ]:


# https://chatgpt.com/share/66ecc158-1ad4-800f-9b98-786672c58857


# In[ ]:


# ChatGPT explains the Monte Hall problem very clearly, 
# including how to set up the list and how to run through the code.
# Its rewrite version shows another way of solving the problems, you can learn from it.
# It explaination of the "Markovian ChatBot" code was too long,
# which makes the reading hard to continue. 
# However, i can still understand the most part.
# in conclusion, ChatBot is a very useful and helpful tool for coding. 
# However, you cannot rely on it too much, since the information it offers is usually too long. 


# In[ ]:


# 7)Initially, I didn’t think that data statistics needed the help of AI tools.
# I thought that it was enough to just use traditional tools such as Excel for calculations.
#vBut in fact, since I took this course, I learned that using coding to perform data statistics can make things very simple and clear.
# And AI is a very easy-to-use tool that can quickly organize and interpret data, greatly reducing the amount of work on people.


# In[ ]:


# https://chatgpt.com/share/66ecd863-c544-800f-8cd3-af24b112cb1b


# In[ ]:


# Somewhat

