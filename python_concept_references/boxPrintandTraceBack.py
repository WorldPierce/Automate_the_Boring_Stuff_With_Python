import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol needs to be of length one.')
    if(width < 2) or (height < 2):
        raise Exception('Width and height must be > 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * width - 2) + symbol)
    print(symbol * width)

boxPrint('*', 10, 5)

# allow code to have errors and continue running while saving message
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt','a')
    errorFile = write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt')

# assertion




    
