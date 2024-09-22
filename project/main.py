# PART 1 - Main Version
# A. Outcomes
def get_outcome(credit_Pass, credit_defer, credit_Fail):
    if credit_Pass + credit_defer + credit_Fail != 120:
        return "Total incorrect."
    if credit_Pass == 120:
        return "Progress"
    elif credit_Pass == 100:
        return "Progress (module trailer)"
    elif credit_Pass >= 80:
        return "Exclude"
    else:
        return "Do not progress – module retriever"


credit_Pass = int(input("Please enter your credits at pass: "))
credit_Fail = int(input("Please enter your credits at fail: "))
credit_defer = int(input("Please enter your credits at defer: "))

print(f"Your Progression Outcome is: {get_outcome(credit_Pass, credit_defer, credit_Fail)}")
