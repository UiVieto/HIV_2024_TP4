def test_file_name_check(file_name_check):
    assert file_name_check("giubfvaewovbaw.dll") == 'Yes'
    assert file_name_check("wadawfsvwe.12") == 'No'
    assert file_name_check("giubfvaewovbaw.dll") == 'Yes'
    assert file_name_check("wadawfsvwe.12") == 'No'
    assert file_name_check("giubfvaewovbaw.dll") == 'Yes'
    assert file_name_check("wadawfsvwe.12") == 'No'
