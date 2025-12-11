import json

def addCard():
    username = input('Enter a username:')
    password = input('Enter a password:')
    ccnum = input('Enter creditcard number:')
    cclimit = input('Enter the limit')
    outstanding = 0
    cc_card = {'username':username,'password':password,'ccnum':ccnum,'limit':cclimit,'outsanding':outstanding}
    with open('ccdata.json','r')as f:
        data=json.load(f)
        data.append(cc_card)
        with open('ccdata.json','w')as f:
            json.dump(data,f,indent=4)
def showCard():
    pass
def SpendCard():
    card_num = input('enter card number:')
    spend_amt = int(input('enter the amount to be spend:'))
def paythebill():
    pass
def main():
    print('Press 1 for Creating a Account , Press 2 for Showing your Credit cards, Press 3 for Spending the Credit Card, Press 4 for Paying the bill')
    ip = int(input('Enter your choice'))
    if ip == 1:
        addCard()
    elif ip == 2:
        showCard()
    elif ip == 3:
        SpendCard()
    elif ip == 4:
        paythebill()
    else:
        print('Enter a valid Choice')
main()