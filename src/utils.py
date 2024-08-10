import subprocess

TITLE = "Books API"
DESCRIPTION = "The Book API Service is a comprehensive API designed to facilitate interaction with book data, making it easy to access, manage, and utilize information about books in a variety of applications. Whether you're building a reading app, a book recommendation system, or a library management tool, our API provides a powerful and flexible solution for handling book-related data."


def latest_tag():
    result = subprocess.run(
        ["git", "describe", "--tags", "--abbrev=0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if result.returncode == 0:
        return result.stdout.strip()
    else:
        raise Exception(f"Error retrieving latest tag: {result.stderr.strip()}")
