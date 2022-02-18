"""Load a text file as a list
Arguments:
    -txt file name (and possibly path)
Exceptions:
    -IOError if filename not found
Returns:
    -a list of all words in a text file in lowercase
Requires:
    import sys

"""
import sys

def lc_strings(file):
    """Open a txt file, return a list of lowercase strings"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e,file),file=sys.stderr)
    sys.exit(1)