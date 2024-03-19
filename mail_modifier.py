def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index=email.index("@"+old_domain)
        new_mail=email[:index]+"@"+new_domain
        print(new_mail)
    return email
replace_domain("sumanthsanju123@gmail.com","gmail.com","google.com")
