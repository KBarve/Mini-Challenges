def add_review(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title,title,rating,name,text):
    ls_review_title.append(title)
    ls_review_rating.append(rating)
    ls_review_text.append(text)
    ls_review_reviewer.append(name)
def delete_review(ls_review_reviewer,ls_review_rating,ls_review_text,ls_review_title,index):
    ls_review_title.pop(index-1)
    ls_review_rating.pop(index-1)
    ls_review_text.pop(index-1)
    ls_review_reviewer.pop(index-1)
