# Your code here
import os



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    mapping = {}

    for filename in files:
        basename = os.path.basename(os.path.normpath(filename))
        if basename in mapping:
            mapping[basename].append(filename)
        else:
            mapping[basename] = [filename]
    
    result = []

    for query in queries:
        if query in mapping:
            result += mapping[query]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
