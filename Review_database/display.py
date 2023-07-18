def Print_reviews_help():
    print('')
    print('Enter the corresponding number to access that command.')
    print('1 : Print all reviews')
    print('2 : Choose a review by index and print the full review')
    print('3 : Add a review')
    print('4 : Delete a review')
    
def Print_all(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title):
    x=0
    print('Index    Title    Rating    Reviewer')
    while x<len(ls_review_title):
        print(f'{x+1}    {ls_review_title[x]}    {ls_review_rating[x]}/10    {ls_review_reviewer[x]}')
        x+=1

def Print_selected(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title,index):
    print(f'{ls_review_title[index-1]} {ls_review_rating[index-1]}/10')
    print(f'Reviewer: {ls_review_reviewer[index-1]}')
    print(f'Review: {ls_review_text[index-1]}')

def demo(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title):
    ls_review_title.extend(['The Boys','Adult Driver','End Of Neon Genesis','Samurai Shampoo'])
    ls_review_rating.extend(['10','10','10','10'])
    ls_review_text.extend(["Hallmark of our generation, perfect film in every way.","Great movie with fast cars, starring Adult Driver Adam Driver.", "Gorgeous, deep plot, trippy visuals.", "Great soundtrack, even better plot and fight choreography."])
    ls_review_reviewer.extend(['Knopp B', 'Gio P', 'Michael Pod', 'Niruth B'])
