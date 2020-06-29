# import the library     
from matplotlib import pyplot as plt
import numpy as np


# plt.style.available fivethirtyeight   
plt.style.use("fivethirtyeight") 

# Age
age = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
indexes = np.arange(len(age))
width = .27

# Median Scientist Salary by Age
s_y = [39496, 43000, 47752, 50320, 54200,
         57000, 63316, 65928, 68317, 69748, 74752]
fig = plt.bar(indexes-width, s_y, width=width, color="r", label="Scientist")



# Median Salaries Of a Computer Scientist by Age 
s_cs_y = [46372, 49876, 54850, 58287, 64016,
            66998, 71003, 71000, 72496, 76370, 84640]
fig = plt.bar(indexes, s_cs_y, width=width, color="b", label="CS")


# Median Salaries Of an engineer by Age
e_y = [38810, 44515, 47823, 50293, 54437,
            58373, 63375, 67674, 69745, 69746, 75583]
fig = plt.bar(indexes+width, e_y, width=width, color="black", label="Engineer")




# change the title  
plt.title("Median Scientist Salary by Age")



# change x axis name  
plt.xlabel("Age")



# change y axis name   
plt.ylabel("Median Salary")


#
plt.xticks(ticks=indexes, labels=age)


# add legend feature   
plt.legend()



# make window fluid tight_layout  
plt.tight_layout()



# save the current graph savefig  
#plt.savefig('image.png')



# show the graph object in the window  
plt.show()

