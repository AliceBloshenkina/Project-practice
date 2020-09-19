import tinder_api.session
import itertools
from datetime import datetime
import tinder_api.work_with_photo as wwp
import tinder_api.classifier as clf
import tinder_api.in_directory as in_drc

sess = tinder_api.session.Session() # inits the session

#print("My _id is %s" %sess.get_id())

#sess.update_profile(bio="VIM is the best")
url_img_person = 'c:\\Users\\ALISA\\Desktop\\Вуз\\Проектная практика\\Фото\\img_person'
url_img_man = 'c:\\Users\\ALISA\\Desktop\\Вуз\\Проектная практика\\Мужчины\\'


answer = input(str('Соберете свой датасет? (да или нет): '))
if answer == 'да':
    print("ok")
    clf.__init__()
    in_drc.__init__(url_img_man)

for user in itertools.islice(sess.yield_users(), 1):
    print('Name: ', user.name) # prints the name of the user see __init__
    # How to check if it exists, if it doesnt, it returns <MisssingValue>
    print('Age: ', user.age)
    if user.bio != "<MissingValue>":
        if user.bio == '':
            print("Doesn't have bio")
        else:
            print('Bio: ', user.bio)
    print('Photo url: ', user.photos)

    len_photos = len(user.photos)
    wwp.__init__(user.photos, url_img_person) # download all photo at the directory
    wwp.in_black(len_photos, url_img_person) # make photo in whote-black color

    print('Match: ', user.like()) # returns false if not a match
    print(' ')


# for match in sess.yield_matches():
#     print(match.name)
#     print(match.match_data) # prints all the match_data
#     print([x.body for x in match.get_messages()]) # gets the body of messages
#     #print(match.message("Hello")) # sends hello to the match


