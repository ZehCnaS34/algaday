
def create_field(dim):
    pass


def main():
    from time import sleep
    import curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    sleep(1)
    
    curses.endwin()

if __name__ == '__main__':
    main()