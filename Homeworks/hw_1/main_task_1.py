def parse(query: str) -> dict:
    parts = query.split("?")
    if len(parts) != 2:
        return {}

    queryParams = parts[1].split("&")

    result = {}
    for param in queryParams:
        paramParts = param.split("=")
        if len(paramParts) != 2:
            continue
        paramName = paramParts[0]
        paramValue = paramParts[1]
        result[paramName] = paramValue
    return result



if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    #
    assert parse('http://example.com/&?name=Dima') == {'name': 'Dima'}
    assert parse('http://123') ==  {}
    assert parse('https://example.com/path/to/page?color=purple') == {'color': 'purple'}
    assert parse('https://example.com/path/to/page?colorrrrrrr=purple') == {'colorrrrrrr': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&surname=surname') == {'name': 'ferret', 'color': 'purple','surname': 'surname'}