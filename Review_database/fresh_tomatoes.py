import sys
from display import *
from operations import *

ls_review_title = []
ls_review_rating = []
ls_review_text= []
ls_review_reviewer = []

if len(sys.argv)==2:
    if sys.argv[1]=='demo':
        demo(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title)

print("Hello, welcome to Fresh Tomatoes! For a list of commands, enter 'help'. To exit, enter 'exit'")

while True:
    inp = input('')
    if inp!='help' and inp!='exit' and inp!='1' and inp!='2' and inp!='3' and inp!='4' and inp!='':
        print(f'Sorry, {inp} is not a valid command.')
    elif inp=='':
        print('Sorry, empty input is not a valid command.')
    elif inp=='exit':
        print('\nExiting. Goodbye!')
        break
    elif inp=='help':
        Print_reviews_help()
    elif inp=='1':
        operation_1(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title)
    elif inp=='2':
        operation_2(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title)
    elif inp=='3':
        operation_3(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title)
    elif inp == '4':
        operation_4(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title)

       










