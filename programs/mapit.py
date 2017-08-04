import webbrowser, sys, pyperclip
# never name file after a module!!!
# import sys for cmd line args
# webbrowser.open('https://automatetheboringstuff.com')

# check if command line args are passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    # https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/' + address)


