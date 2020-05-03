from faker import Faker

def users_addres(length: int=100):
    fake = Faker()
    adress_result = ''

    for i in range(length):
        adress_result += (fake.name() + ' ' + fake.email() + '\n')
    return adress_result