from colorama import Fore, Style, init

class ColorOutput:
    def __init__(self):
        init()
    
    @staticmethod
    def red(message):
        print(f"{Fore.RED}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def green(message):
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def yellow(message):
        print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def blue(message):
        print(f"{Fore.BLUE}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def cyan(message):
        print(f"{Fore.CYAN}{message}{Style.RESET_ALL}")

    @staticmethod
    def magenta(message):
        print(f"{Fore.MAGENTA}{message}{Style.RESET_ALL}")

