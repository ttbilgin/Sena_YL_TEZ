def outer():
    message = 'local'
    def inner():
        nonlocal message
        message = 'nonlocal'
        prnt('inner:', message)
    inner()
    print('outer:', message)
outer()
