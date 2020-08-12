# Default value for parameter and Named parameters
def wish(name="Guest", message="Good Morning"):
    print(message, name)


wish("Steve", "Hello")  # Positional
wish("Eric")
wish()
wish(message="Hello")  # Keyword argument
wish(message="Hello", name='Scott')  # Keyword argument
