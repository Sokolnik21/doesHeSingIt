"""
Requires:
    Based on URL, module downloads full text of the song

Used additional libraries:
    newspaper:
        https://github.com/codelucas/newspaper
"""

import Parser
import HTMLConfiguration
from newspaper import Article


def getFullSong():
    result = ""
    url = HTMLConfiguration.createHtml(Parser.getAuthor(), Parser.getTitle())

    # making class object Article
    article = Article(url)

    # downloading web page to the class
    article.download()

    # parsing the source code
    article.parse()
    # it is needed to dig into the source code of web page to get song text

    # getting source code from article and splitting it by <h2>
    # <h2> is a header which contains song text
    list = article.html.split("<h2>")

    # by splitting code in half the song is now in the second part,
    # that's why list[1] is used later
    # a part of the page which contains song ends with <p> parameter
    list = list[1].split("<p>")

    # after splitting the song is in list[0]
    # but it also contains some <br /> elements which have to be deleted
    list = list[0].split("<br />")

    # first element is not a part of the song
    # (it's some kind of a web page header) ->
    # that's why we start with second element (list[1:])
    # the rest elements is contained into string
    # and divided by " " (<- it's space)
    for elem in list[1:]:
        result = result + elem + " "
    return result
