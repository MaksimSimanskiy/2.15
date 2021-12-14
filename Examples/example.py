#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    try:
        fileptr = open("file.txt")
        # perform file operations
    finally:
        fileptr.close()
