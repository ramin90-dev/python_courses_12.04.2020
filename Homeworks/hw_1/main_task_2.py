def parse_cookie(query:str)->dict:
    queryParams = query.split(";")

    result = {}
    for param in queryParams:
        paramParts = param.split("=")
        if len(paramParts)!=2:
            continue
        paramName = paramParts[0]
        paramValue = paramParts[1]
        result[paramName] = paramValue
    return result



if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('name=Dima') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;age=28') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name') == {}
    assert parse_cookie(';') == {}
    assert parse_cookie('name=Dima;age=28;text=text') == {'name': 'Dima', 'age': '28', 'text':'text'}
    assert parse_cookie('name=&Dima&;') == {'name': '&Dima&'}
    assert parse_cookie('name=Dima; = ;text=text') == {'name': 'Dima', ' ': ' ', 'text':'text'}