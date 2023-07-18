from display import *
from review_storage import *
def operation_1(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title):
    if len(ls_review_title)==0:
        print('No reviews found.')
        Print_reviews_help()
    else:
        print('')
        print('Printing all reviews...')
        Print_all(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title)
        Print_reviews_help()

def operation_2(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title):
    if len(ls_review_title)==0:
            print('No reviews found.')
            Print_reviews_help()
    else:
        print('')
        print('Select a review by index to print the full review!')
        print('Printing all reviews...')
        
        Print_all(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title)
        while True:
            index = int(input(''))
            if index>len(ls_review_title) or index<=0:
                print('Invalid index, try again!')
            elif index<=len(ls_review_title):
                Print_selected(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title,index)
                Print_reviews_help()
                break

def operation_3(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title):
    print('')
    print('Review add mode...')

    title = input('Please enter the title of the movie: ')
    while title=='':
        if title=='':
            title = input('Invalid title. Please enter the title of the movie: ')
        else:
            break
    rating = input('Please enter the rating of the movie out of 10: ')
    while int(rating)>10 or int(rating)<0:
        if int(rating)>10 or int(rating)<0:
            rating = input('Invalid rating. Please enter the rating of the movie out of 10: ')
        else:
            break
    name = input('Please enter the name of the reviewer: ')
    while name=='':
        if name=='':
            name = input('Invalid reviewer name. Please enter the name of the reviewer: ')
        else:
            break
    text = input('Please enter the textual review: ')
    while text=='':
        if text=='':
            text = input('Invalid textual review. Please enter the textual review: ')
        else:
            break

    print('Printing input review...')
    index = len(ls_review_rating)
    print(title+' '+rating+'/10')
    print('Reviewer: '+ name)
    print('Review: '+text)
    choice = input('Do you want to add the following review to the database? y/n ')
    while True:
        if choice=='y':
            add_review(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title,title,rating,name,text)
            print('Review added!')
            print('Exiting review add mode...')
            Print_reviews_help()
            break
        elif choice=='n':
            print('Review dumped')
            print('Exiting review add mode...')
            Print_reviews_help()
            break
        else:
            choice = input('Invalid input: Do you want to add the following review to the database? y/n ')


def operation_4(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title):
    if len(ls_review_title)==0:
        print('No reviews found.')
        Print_reviews_help()
    else:
        print('')
        print('Review delete mode...')
        print('Select a review by index to delete it.')
        print('Printing all reviews...')
        Print_all(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title)

        index = 0
        while index>len(ls_review_title) or index<=0:
            index = int(input(''))
            if index>len(ls_review_title) or index<=0:
                print('Invalid index, try again!')
            if index<=len(ls_review_title) and index>0:
                break
        
        if index<=len(ls_review_title) and index>0:
            print('')
            print('Delete the selected review? y/n')
                    
            Print_selected(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title,index)
            
            
            choice = input('')
            while True:
                if choice == 'y':
                    delete_review(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title,index)
                    print('Review deleted.')
                    print('Exiting review delete mode...')
                    Print_reviews_help()
                    break
                elif choice == 'n':
                    print('Review not deleted.')
                    print('Exiting review delete mode...')                            
                    Print_reviews_help()
                    break
                else:
                    choice = input('Invalid input: Do you want to delete the selected review? y/n ')












