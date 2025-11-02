# tests/models/test_link_model_fields.py
from links.models import Link

def test_title_field_type():
    field = Link._meta.get_field("title")
    assert field.get_internal_type() == "CharField"
