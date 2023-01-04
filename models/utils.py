from re import sub


def slugify(s):
    pattern = r'[^\w+]'
    return sub(pattern, '-', s).lower()