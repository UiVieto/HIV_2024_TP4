def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("fail.12") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("fail.12") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("fail.12") == 'No'
