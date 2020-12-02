test_list = [1, 4, 5, 6, 3, 10] 
  
# printing original list  
print ("The original list is : " + str(test_list)) 
  
# First naive method 
# using loop method to print last element  
for i in range(0, len(test_list)): 
  
    if i == (len(test_list)-1): 
        print ("The last element of list using loop : "+  str(test_list[i])) 
  
# Second naive method         
# using reverse method to print last element 
test_list.reverse() 
print("The last element of list using reverse : "
                            +  str(test_list[0])) 