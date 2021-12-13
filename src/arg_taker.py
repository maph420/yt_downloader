import sys
argsList=["-s","-d","--search","--download","-h","--help"]

class unknown_parameter(Exception):
    pass

def helpDisplay():
    print("\n--------------------------------------")
    print("\tYT DOWNLOADER")
    print("\tmade by maph")
    print("--------------------------------------\n")
    print("->Help:\npython yt.py -h // python yt.py --help\n")
    print("->Download a video given its url:\npython yt.py -d <url_goes_here> // python yt.py --download <url_goes_here>\n")
    print("->Look for a video through a YouTube search within the CLI:\npython yt.py -s <num_of_results_you_are_looking_for> // python yt.py --search <num_of_results_you_are_looking_for>")
    print("\n(you can simply write python yt.py -s // python yt.py --search so 10 results will be displayed as default)\n")
    exit()


def main():
    if len(sys.argv) < 2:
        print("Error: Too few arguments, try again\nUsage: 'python yt.py <instruction> <arg>'")
        exit()
    else:
        arg = sys.argv[1]

    for a in argsList:
        if a == arg:
            return arg
    raise unknown_parameter

if __name__ == "__main__":
   x = main()