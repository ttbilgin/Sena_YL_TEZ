def myFunc(e):
    return len(e)
cars = ['Ford', 'Mitsubishi',  'VW']
cars.sort(reverse=True, key=myFunc)