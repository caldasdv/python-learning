# to receive a input from the terminal we use the input("whatyouwant: ") function

## a string receive example:

name = input("what's your name? ")

print(f'nice to meet you {name}!')

# we can manipule the end of a print with diferent ways, like: sep, end, file, flush

## There are some examples:

nickname = input("what's your nickname? ")

### the comum way

print(name, nickname)

### using end

print(name, nickname, end = "...\n")

### using sep

print(name, nickname, sep="#")

### with file we can export the print to a atual file, in this cade output.txt

with open('output.txt', 'w') as f: #creating/opennig the file
    print(name, nickname, file=f) #passing the info to the file f

### using flush

print('Hello', flush=True)

# Output: Hello (flushed immediately)

