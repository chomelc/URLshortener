#!/usr/bin/env python3
import pyshorteners
import pyperclip
import sys

class URL:
    longURL = ""
    shortURL = ""

    def getURL(self):
        self.longURL = sys.argv[1]

    def shortenURL(self):
        self.getURL()
        shortener = pyshorteners.Shortener()
        self.shortURL = shortener.tinyurl.short(self.longURL)

    def copyToClipboard(self):
        pyperclip.copy(self.shortURL)

if __name__ == "__main__":
    url = URL()
    url.shortenURL()
    print(f"Copying '{url.shortURL}' to clipboard.")
    url.copyToClipboard()