def car_count(data:list, name:'str')->int:
    for item in data:
        if item['ner']==name:
            return len(item['mashinuud'])