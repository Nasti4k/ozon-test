from functions_superhero import get_tallest_hero

def test_male_with_job():
    result=get_tallest_hero("Male", True)
    assert result is not None
    assert isinstance(result, str)

def test_other_info():
    result = get_tallest_hero("Other", True)
    assert result is None

def test_femail_job():
    result = get_tallest_hero("Female", False)
    assert result is not None

def test_mail_withe_job():
    assert get_tallest_hero("Male", True)=="Utgard-Loki"