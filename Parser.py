import argparse


def parser():
    parser = argparse.ArgumentParser()

    # Phrase
    parser.add_argument("phrase",
                        help="Phrase you want to check whether it is in song")

    # SongAuthor
    parser.add_argument("author",
                        help="Music band")

    # SongAuthor
    parser.add_argument("title",
                        help="Music title")

    return parser.parse_args()


def getPhrase():
    args = parser()
    return args.phrase


def getAuthor():
    args = parser()
    return args.author


def getTitle():
    args = parser()
    return args.title
