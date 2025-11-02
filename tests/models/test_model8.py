from links.forms import LinkForm

def test_description_is_required():
    form = LinkForm(data={
        "title": "My Link",
        "url": "https://example.com",
        "description": ""  # left blank
    })
    assert not form.is_valid()
    assert "description" in form.errors
