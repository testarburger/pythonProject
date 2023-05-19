def my_mood(answear):
    print("My mood today:")
    print(answear)
resp = input("How are you?")
my_mood(resp)
print("*********")
def my_mood2(answear2):
    return answear2*2
resp2=input("How are you?")
twiced = my_mood2(resp2)
print("My mood is like", twiced)