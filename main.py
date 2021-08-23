#!/usr/bin/env python3

""""This is the main file."""

import logging


def main():
    logging.basicConfig(filename="main.log",
                        format='%(asctime)s %(levelname)s: %(message)s',
                        filemode="w",
                        level=logging.INFO)
    logging.info('Started')

    logging.info('Finished')


if __name__ == "__main__":
    main()
 
