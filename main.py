from utils import Hash

def run(login_information):
    hashid = Hash()
    return_userid = []
    for login in login_information:
        company_source_code = acquire_code(login.company_name, login.source)
        user_code = hashid.encode(login.user)
        return_userid.append(company_source_code + user_code)
        print





if __name__ == '__main__':
    login_information = input('please provide login information')
    result = run(login_information)
    print(result)
