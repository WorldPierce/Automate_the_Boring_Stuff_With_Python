import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # disable all log levels critical or lower(so all of them)
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start if factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))
logging.debug('End of program')

#can save log messages to file if you add filename="relativeFile.txt" to beginng of basic config
