from glob import glob

from datetime import date


def change_string_in_file(filename: str, old_string: str, new_string: str):
    """Replaces old_string with new_string from filename and saves the result to that file"""
    with open(filename) as f:
        content = f.read()

    if old_string not in content:
        return

    with open(filename, 'w') as f:
        content = content.replace(old_string, new_string)
        f.write(content)


files = glob("./_build/html/**/*html", recursive=True)

for file in files:
    change_string_in_file(file, "fa-github", "fa-gitlab")
    change_string_in_file("./_build/html/README.html", "|version_placeholder|", str(date.today()))
