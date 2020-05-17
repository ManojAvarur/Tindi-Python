import shelve as s

op = s.open('bin/test.bd')

yest = op['yestrdayList']

def setDays(x):
    check = False
    if x < (len(yest) - 2):
        reset()
        check = True

    op['days'] = x
    return check

def retriveDays():
    x = op['days']
    return x

def dayCount():
    return ( len(yest) - 2 ) 

def appi(x):
    yest.append(x)

def reset():
    global yest
    yest = [0, 0]

def update():
    op['yestrdayList'] = yest

def prt():
    return yest

# def prtlastlen():
    # return (len(yest))


