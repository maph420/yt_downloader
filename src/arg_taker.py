import sys
import argparse
argsList=["-s","-d","--search","--download","-h","--help"]

class unknown_parameter(Exception):
    pass

def helpDisplay():
    print("\n--------------------------------------")
    print("\tYT DOWNLOADER")
    print("\tmade by maph")
    print("--------------------------------------\n")

    print("usage: python yt.py [args] <optional args>")

    print("General options\n")
    print("-h , --help\n\tshow this help message and exit\n\n")
    print("-d [video_url_goes_here], --download [video_url_goes_here]\n\tdownload a video given its url\n\n")
    print("-s [video_title] <num_of_results_to_be_searched>, --search [video_title] <num_of_results_to_be_searched>\n\tMake a youtube search within the CLI given a video's title")
    print("\t(You can ommit the <num_of_results_to_be_searched> arg though, then 10 results will be displayed as default)\n")
    exit()


def main():
    if not (sys.argv[1]=='-h' or sys.argv[1]=='--help') and len(sys.argv) < 3:
        print("Error: Too few arguments, try again\nYou can look for help with: 'python yt.py -h'")
        exit()
    else:
        arg = sys.argv[1]

    for a in argsList:
        if a == arg:
            return arg
    raise unknown_parameter

if __name__ == "__main__":
   x = main()