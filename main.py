user_input_no_test = input("\nHow many tests have you taken: ")
if user_input_no_test.isnumeric() == False:
        print("\ninvalid entry")
        quit()

no_test = int(user_input_no_test)


user_input_test_weight = input("\nTest Weight: ")
if user_input_test_weight.isnumeric() == False:
        print("\ninvalid entry")
        quit()

user_weight = float(user_input_test_weight)
test_weight = user_weight/100

x = 0

user_score_list = []
total = 0
while x < no_test:

        if no_test >= 1:
                user_input_test_score = input("\nScore #%d: " %(x+1))

                if user_input_test_score.isnumeric() == False:
                        print("\ninvalid entry")
                        quit()

                user_test_score = float(user_input_test_score)
                x +=1
                user_score_list.append(user_test_score)
                print(user_score_list)

                add_total_test = sum(user_score_list)
                mult_by_weight = add_total_test*test_weight
                add_total_test = mult_by_weight/no_test
