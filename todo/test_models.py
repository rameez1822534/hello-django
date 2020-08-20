from django.test import TestCase
from .forms import itemForm


class TestitemForm(TestCase):

    def test_item_name_is_required(self):
        form = itemForm ({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = itemForm ({'name': 'test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = itemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
