Test = True

user_input_test_weight = input("\nTest Weight(divide by 100): ")
test_weight = float(user_input_test_weight)

user_input_test_score = input("Test Score: ")
test_score = float(user_input_test_score)

test_final_score = test_score*test_weight

#----------------------------------------------------------------------------------------
Assignment = True

user_input_assignment_weight = input("\nAssignment Weight(divide by 100): ")
user_input_assignment_score= input("Assignment Score: ")

assignment_weight = float(user_input_assignment_score)
assignment_score = float(user_input_assignment_score)

assignment_final_score = assignment_score*assignment_weight

if Test and Assignment == True:
                final_grade = assignment_final_score+test_final_score
                print( str("final grade: ") + str(final_grade))








