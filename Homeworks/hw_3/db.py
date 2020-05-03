import sqlite3

def run_query(query: str)->list:
    conn = sqlite3.connect('./chinook.db')
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    return result

def ordering(query_param: str)->str:
    result = []
    for elem in query_param.split(','):
        if '-' in elem:
            result.append(f'{elem[1:].capitalize()} DESC')
        else:
            result.append(elem.capitalize())
    return ', '.join(result)

if __name__=='__main__':
    assert ordering('country,-city')== 'Country, City DESC'
    assert ordering('-country,-city')== 'Country DESC, City DESC'
    assert ordering('')== ''
