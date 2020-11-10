check = True
jab = input("\nTest Weight: ")

if jab.isnumeric()== False:
        print("\nuse numbers")
        quit()



job = input("Test Score: ")
test_weight = float(jab)

if job.isnumeric() == False:
        print("\nuse numbers")
        quit()

test_worth = test_weight/100
test_score = float(job)

test_final_score = test_score*test_worth


chock = True
jyb = input("\nAssignment Weight: ")

if jyb.isnumeric()== False:
        print("\nuse numbers)")
        quit()

job = input("Assignment Score: ")


assignment_weight = float(jab)
assignment_worth = assignment_weight/100

if job.isnumeric() == False:
        print("\nuse numbers")
        quit()


assignment_score = float(job)

assignment_final_score = assignment_score*assignment_worth

if check and chock == True:
                final_grade = assignment_final_score +test_final_score
                print( str("\nfinal grade: ") + str(final_grade))








