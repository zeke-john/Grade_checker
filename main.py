user_input_parts_grade = input("\nHow many parts is your grade divivded in: ")
if user_input_parts_grade.isnumeric() == False:
        print("\ninvalid entry")
        quit()

user_parts_grade= int(user_input_parts_grade)


y = 0
total_list = [] 
while y < user_parts_grade:
        user_input_no_Assignments = input("\nHow many Assignments have you taken for this part: ")
        if user_input_no_Assignments.isnumeric() == False:
                print("\ninvalid entry")
                quit()

        no_Assignments = int(user_input_no_Assignments)


        user_input_Assignments_weight = input("\nAssignments Weight: ")
        if user_input_Assignments_weight.isnumeric() == False:
                print("\ninvalid entry")
                quit()

        user_weight = float(user_input_Assignments_weight)
        Assignments_weight = user_weight/100

        x = 0

        user_score_list = []
        total = 0
        while x < no_Assignments:

                if no_Assignments >= 1:
                        user_input_Assignments_score = input("\nScore #%d: " %(x+1))
                        
                        if user_input_Assignments_score.isnumeric() == False:
                                print("\ninvalid entry")
                                quit()

                        user_Assignments_score = float(user_input_Assignments_score)
                        x +=1
                        user_score_list.append(user_Assignments_score)

                        add_total_Assignments = sum(user_score_list)
                        mult_by_weight = add_total_Assignments*Assignments_weight
                        add_total_Assignments = mult_by_weight/no_Assignments
        y += 1

        total_list.append(add_total_Assignments)
        add_total_grade = sum(total_list)
        
print(str("\nTotal Grade: ") + str(add_total_grade) + str("%"))