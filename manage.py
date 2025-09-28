#!/usr/bin/env python
import os
import sys

"""Project management entrypoint.

This project uses a nested Django package at `movie_tracker/movie_tracker`.
Rely on Django's module import via DJANGO_SETTINGS_MODULE instead of manual path hacks.
"""

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_tracker.movie_tracker.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
