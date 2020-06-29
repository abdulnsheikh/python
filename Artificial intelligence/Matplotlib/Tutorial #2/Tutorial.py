# import the library     
from matplotlib import pyplot as plt



# plt.style.available fivethirtyeight   
plt.style.use("fivethirtyeight") 


# Median Scientist Salary by Age
s_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
s_y = [39496, 43000, 47752, 50320, 54200,
         57000, 63316, 65928, 68317, 69748, 74752]
fig = plt.plot(s_x, s_y, color="r", label="Median Scientist Salary ", marker="o", markerfacecolor="w", markersize=12, linestyle=":")



# Median Salaries Of a Computer Scientist by Age
s_cs_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
s_cs_y = [46372, 49876, 54850, 58287, 64016,
            66998, 71003, 71000, 72496, 76370, 84640]
fig = plt.plot(s_cs_x, s_cs_y, color="b", label="Median CS Salary ", marker="v", markerfacecolor="b", markersize=12, linestyle=":")



# change the title  
plt.title("Median Scientist Salary by Age")



# change x axis name  
plt.xlabel("Age")



# change y axis name   
plt.ylabel("Median Salary")



# add legend feature   
plt.legend()



# make window fluid tight_layout  
plt.tight_layout()



# save the current graph savefig  
#plt.savefig('image.png')



# show the graph object in the window  
plt.show()

