
class Util:
    def sPrint(*args):
        """
        Concats all argumetns and prints them as string (delim not included). \n\n
        any *args
        """
        res = ""
        for e in args:
            res += str(e)
        print(res)

    def wrapColor(text, color):
        """
        Wraps text in ASCI colours for terminal usage.
        see colours in Util.colors for simple selection, argument accepts ANCI code like "\\x1b[0;34;42".
            See Util project Main class' printAllColours function for most or all styles.
        string text
        string/int color
        """
        colorArg = ""

        if(Util.isInt(str(color))):
            colorList = list(Util.colors)
            if(int(color) < 0 or int(color) > len(colorList) - 1):
                return "Color index out of range (0 - " + str(len(colorList) - 1) + ")"

            colorArg = Util.colors[colorList[int(color)]]
        elif(str(color[0]) == "\x1b"):
            colorArg = color
        else:
            colorArg = Util.colors[str(color)]

        return colorArg + str(text) + Util.colors["ENDC"]

    # https://note.nkmk.me/en/python-check-int-float/
    def isInt(n):
        """
        Try parse n as float or inter, return true/false
        n value attempt to parse to number
        """
        try:
            float(n)
        except ValueError:
            return False
        else:
            return float(n).is_integer()

    colors = {
        "HEADER": "\x1b[95m",
        "OKBLUE": "\x1b[94m",
        "OKGREEN": "\x1b[92m",
        "WARNING": "\x1b[93m",
        "FAIL": "\x1b[91m",
        "ENDC": "\x1b[0m",
        "BOLD": "\x1b[1m",
        "UNDERLINE": "\x1b[4m",
    }