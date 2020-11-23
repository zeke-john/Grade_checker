user_input_parts_grade = input("\nHow many parts is your grade divivded in: ")

while user_input_parts_grade.isnumeric() == False:
        print("\ninvalid entry")
        user_input_parts_grade = input("\nHow many parts is your grade divivded in: ")
        


user_parts_grade= float(user_input_parts_grade)


y = 0
total_list = [] 
while y < user_parts_grade:
        user_input_no_Assignments = input("\nHow many Assignments have you taken for this part: ")

        while user_input_no_Assignments.isnumeric() == False:
                print("\ninvalid entry")
                user_input_no_Assignments = input("\nHow many Assignments have you taken for this part: ")

        no_Assignments = int(user_input_no_Assignments)

        user_input_Assignments_weight = input("\nAssignments Weight: ")


        try:
                user_weight = float(user_input_Assignments_weight)
                Assignments_weight = user_weight/100

        except:
                print("\ninvalid entry")
                user_input_Assignments_weight = input("\nAssignments Weight: ")

        x = 0

        user_score_list = []
        total = 0
        while x < no_Assignments:

                user_input_Assignments_score = input("\nScore #%d: " %(x+1))
                
                try:
                        user_Assignments_score = float(user_input_Assignments_score)
                        x +=1
                        user_score_list.append(user_Assignments_score)

                        add_total_Assignments = sum(user_score_list)
                        mult_by_weight = add_total_Assignments*Assignments_weight
                        add_total_Assignments = mult_by_weight/no_Assignments
                except:
                        print("\ninvalid entry")
                        
        y += 1

        total_list.append(add_total_Assignments)
        add_total_grade = sum(total_list)

        if y == user_parts_grade:
                print(str("\nTotal Grade: ") + str(add_total_grade) + str("%"))