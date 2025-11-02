# tests/forms/test_linkform_labels.py
from links.forms import LinkForm

def test_title_label():
    form = LinkForm()
    assert form.fields["title"].label == "Title"
