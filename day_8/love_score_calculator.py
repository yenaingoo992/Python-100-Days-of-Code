def calcualte_love_score(your_name: str, partner_name: str):
    name = (your_name + partner_name).lower()
    true_score = 0
    love_score = 0
    
    for letter in "true":
        true_score += name.count(letter)
    
    for letter in "love":
        love_score += name.count(letter)
    
    total_score = (true_score * 10) + love_score
    
    print(f"Your love score is {total_score}")