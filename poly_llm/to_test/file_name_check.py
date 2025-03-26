
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'

def test_file_name_check(): # pragma: no cover
    assert file_name_check("example.txt") == 'Yes' # pragma: no cover
    assert file_name_check("1example.dll") == 'No' # pragma: no cover
    assert file_name_check('.txt') == 'No'# pragma: no cover

    # Tests zero shot générés par Salesforce/codet5-large-ntp-py
    # assert file_name_check('file_name.txt') == 'Yes' # pragma: no cover
    # assert file_name_check('file_name.exe') == 'Yes' # pragma: no cover
    # assert file_name_check('file_name.dll') == 'Yes' # pragma: no cover
    # file_name_check('file_name.txt.exe') == 'Yes' # pragma: no cover
    # file_name_check('file_name.txt.dll') == 'Yes' # pragma: no cover
    # file_name_check('file_name.exe.dll') == 'Yes' # pragma: no cover
    # file_name_check('file_name.exe.txt') == 'Yes' # pragma: no cover
    # file_name_check('file_name.exe.dll.txt') == 'Yes' # pragma: no cover
    # file_name_check('file_name.exe.dll.exe.txt') == 'Yes' # pragma: no cover
    # file_name_check('file_name.exe.dll.exe.exe.txt') == 'Yes' # pragma: no cover
    # file_name_check('file_name.exe.dll.exe.exe.exe.txt') == 'Yes' # pragma: no cover
    # file_name_check('file_name.exe.dll.exe.exe.exe.exe.txt') == 'Yes' # pragma: no cover
    # file_name_check('file_name.exe.dll.exe.exe.exe.exe.exe.txt') == 'Yes' # pragma: no cover

    # Tests few shot générés par Salesforce/codet5-large-ntp-py
    # assert file_name_check("test.txt") == 'Yes' # pragma: no cover
    # assert file_name_check("test.exe") == 'Yes' # pragma: no cover
    # assert file_name_check("test.dll") == 'Yes' # pragma: no cover

    # Test générés avec Qwen2.5-Coder-0.5B-Instruct
    assert file_name_check("example.txt") == 'Yes' # pragma: no cover
    assert file_name_check("example.exe") == 'Yes' # pragma: no cover
    assert file_name_check("example.dll") == 'Yes' # pragma: no cover
    assert file_name_check("example") == 'No' # pragma: no cover

