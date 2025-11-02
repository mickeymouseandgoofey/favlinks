from links.forms import LinkForm

def test_title_is_required():
    form = LinkForm(data={"url": "https://example.com"})
    assert not form.is_valid()
    assert "title" in form.errors
