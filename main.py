user_input_no_test = input("\nHow many tests have you taken: ")
no_test = int(user_input_no_test)


user_input_test_weight = input("\nTest Weight: ")
user_weight = int(user_input_test_weight)
test_weight = user_weight/100

x = 1
for x in range(no_test):
    user_input_test_score = input("\nWhat score did you get on the " +str(x+1) + str(" one: "))
    test_score = float(user_input_test_score)
    print(test_score)
    x += 1


