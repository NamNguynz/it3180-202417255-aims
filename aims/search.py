def search_by_title(items, keyword):
    return [
        item for item in items 
        if keyword.lower()  in item.title.lower()
    ]