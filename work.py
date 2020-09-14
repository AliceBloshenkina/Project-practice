import tinder_api.session
import itertools
from datetime import datetime
sess = tinder_api.session.Session() # inits the session

#print("My _id is %s" %sess.get_id())

#sess.update_profile(bio="VIM is the best")

for user in itertools.islice(sess.yield_users(), 3):
    print('Name: ', user.name) # prints the name of the user see __init__
    # How to check if it exists, if it doesnt, it returns <MisssingValue
    print('Age: ', user.age)
    if user.bio != "<MissingValue>":
        if user.bio == '':
            print("Doesn't have bio")
        else:
            print('Bio: ', user.bio)
    print('Photo url: ', user.photos)
    print('Match: ', user.like()) # returns false if not a match
    print(' ')


# for match in sess.yield_matches():
#     print(match.name)
#     print(match.match_data) # prints all the match_data
#     print([x.body for x in match.get_messages()]) # gets the body of messages
#     #print(match.message("Hello")) # sends hello to the match


