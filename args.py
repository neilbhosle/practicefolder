
def countries(*country_names):
    print(country_names)
    for n in country_names:
        print("Country: ",n)


countries("India","US","Singapore","Qatar")

def capital(**capital_names):
    print(capital_names)
    for key,value in capital_names.items():
        print("Country {} has capital {}".format(key,value))


capital(India = "Delhi", US = "Washington D.C", Singapore = "Singapore", Qatar = "Doha")