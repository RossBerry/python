"""
chunks.py

Contains chunks generator that breaks a list up into
n-sized chunks
"""


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == "__main__":
    TEST_LIST = [str(n) for n in range(100)]
    for chunk in chunks(TEST_LIST, 2):
        print(chunk)
