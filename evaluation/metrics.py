def quality_score(text):

    score = 100 # starts with full score
    words = len(text.split()) # count the number of words in text
    # if the text is too short it reduce score
    if words < 5:
        score -= 15
    if "I think" in text:
        score -= 10
    if "maybe" in text:
        score -= 10
    # if there are double dots it reducce score
    if ".." in text:
        score -= 5
    # if text is too long, reduce score
    if len(text) > 500:
        score -= 10
     # we should make sure score does not go below 0
    return max(score, 0)