"""
chunks.py

Contains chunks generator that breaks a list or string into n-sized chunks
"""
__author__ = "Kenneth Berry"
__copyright__ = "Copyright 2019, Kenneth Berry"

from typing import Generator, Union


def chunks(obj: Union[list, str], size: int) -> Generator[Union[list, str], None, None]:
    """ Yield successive chunks from list or string. """
    for i in range(0, len(obj), size):
        yield obj[i:i + size]


def test(test_objects: list, size: int) -> None:
    """ Test chunks function with list and string test objects. """
    for test_object in test_objects:
        for chunk in chunks(test_object, size):
            print(chunk)


if __name__ == "__main__":
    TEST_OBJECTS = [[str(n) for n in range(100)], "0123456789" * 10]
    test(TEST_OBJECTS, 10)
