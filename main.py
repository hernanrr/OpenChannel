#!/usr/bin/env python3

""""This is the main file."""

import logging
from logconfig import log_actions


@log_actions
def main():
    logging.info('Started')
    print('Hello world!')
    logging.info('Finished')


if __name__ == "__main__":
    main()
