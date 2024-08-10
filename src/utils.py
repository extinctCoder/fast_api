import os
from os import environ
from os.path import isfile
from pathlib import Path
from subprocess import PIPE, run

TITLE = "Books API"
DESCRIPTION = "The Book API Service is a comprehensive API designed to facilitate interaction with book data, making it easy to access, manage, and utilize information about books in a variety of applications. Whether you're building a reading app, a book recommendation system, or a library management tool, our API provides a powerful and flexible solution for handling book-related data."
CONTACT = {
    "name": "Sabbir Ahmed Shourov",
    "url": "https://www.github.com/extinctCoder",
    "email": "write2shourov@gmail.com",
}
SERVERS = [
    {"url": "http://127.0.0.1:8000", "description": "Local development server"},
    {"url": "http://app_server:8000", "description": "Docker internal Server"},
]


def latest_tag():
    if Path(".version").is_file:
        return Path(".version").read_text().strip().lstrip("v")

    result = run(
        ["git", "describe", "--tags", "--abbrev=0"], stdout=PIPE, stderr=PIPE, text=True
    )
    if result.returncode == 0:
        return result.stdout.strip().lstrip("v")
    else:
        return "unknown version"
