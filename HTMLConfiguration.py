"""
Due to convention of this side (tekstowo.pl)
it is needed to create html this way:
http://www.tekstowo.pl/piosenka,[BAND_NAME],[SONG_TITLE].html
    however there is a hidden rule
    that every letters in BAND_NAME and SONG_TITLE should be in lowercase
    and every space and brackets are changed into "_"
"""


def createHtml(author, title):
    beginning = "http://www.tekstowo.pl/piosenka,"
    middle = author + ',' + title
    ending = ".html"

    result = beginning + middle + ending
    return result
