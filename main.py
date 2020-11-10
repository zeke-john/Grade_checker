user_input_test_weight = input("\nTest Weight(divide by 100): ")
test_weight = float(user_input_test_weight)

user_input_test_score = input("Test Score: ")
test_score = float(user_input_test_score)

test_final_score = test_score*test_weight


final_grade = test_final_score
print( str("final grade: ") + str(final_grade))






