#!/usr/bin/env python
import os
import sys

# Add outer movie_tracker folder to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'movie_tracker'))

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_tracker.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
