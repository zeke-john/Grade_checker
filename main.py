user_input_parts_grade = input("\nHow many parts is your grade divivded in: ")

while user_input_parts_grade.isnumeric() == False:
        print("\ninvalid entry")
        user_input_parts_grade = input("\nHow many parts is your grade divivded in: ")
        
user_parts_grade= float(user_input_parts_grade)

y = float(0)
final_list = []

while y < user_parts_grade:

        user_input_Assignments_points_total_for_class = input("\nTotal number of points this part of the class is worth: ")

        try:
                user_total_points_for_class = float(user_input_Assignments_points_total_for_class)

        except:
                print("\ninvalid entry")
                user_input_Assignments_points_total_for_class = input("\nTotal number of points this class is worth: ")


        user_input_Assignments_weight = input("\nHow much are assignments weighted for this part: ")

        try:
                user_weight = float(user_input_Assignments_weight)
                Assignments_weight = user_weight/100

        except:
                print("\ninvalid entry")
                user_input_Assignments_weight = input("\nHow much are assignments weighted for this part: ")



        user_input_no_Assignments = input("\nHow many Assignments have you taken for this part: ")

        while user_input_no_Assignments.isnumeric() == False:
                print("\ninvalid entry")
                user_input_no_Assignments = input("\nHow many Assignments have you taken for this part: ")

        no_Assignments = int(user_input_no_Assignments)


        x = 0

        p = 0

        user_point_list_add_beg = []
        user_point_list_add_end = []
        total = 0
        while x < no_Assignments:


                user_input_Assignments_points = input("\nNumber of Points you got for assignment #%d: " %(x+1))

                try:

                        user_Assignments_points = float(user_input_Assignments_points)
                        x +=1
                        user_point_list_add_beg.append(user_Assignments_points)
                        user_point_list_add_beg_sum = sum(user_point_list_add_beg)
                        div_user_point_list_add_beg_sum = user_point_list_add_beg_sum / user_total_points_for_class
                        mult_by_weight = div_user_point_list_add_beg_sum * Assignments_weight
                        user_point_list_add_end.append(mult_by_weight)
                        get_thing_we_need = user_point_list_add_end[-1]# last num that has total
                except:
                        print("\ninvalid entry")

                        
        y += 1
        final_list.append(get_thing_we_need)
        final_dec_score = sum(final_list)
        final = final_dec_score * 100
        
print(str("\nTotal Grade: ") + str(final) + str("%"))