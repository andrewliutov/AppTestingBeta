import builtins
import mock
from task_1_docs_app_test import app_full


class TestDocsApp:

    def test_get_doc_owner_name(self):
        with mock.patch.object(builtins, 'input', lambda x: '2207 876234'):
            assert app_full.get_doc_owner_name() == "Василий Гупкин"

    def test_add_new_doc(self):
        inputs = ['101101', 'паспорт', 'Джейсон Стетхем', '1']
        def make_multiple_inputs(inputs):
            def next_input(_):
                return inputs.pop(0)
            return next_input
        with mock.patch.object(builtins, 'input', make_multiple_inputs(inputs)):
            assert app_full.add_new_doc() == '1'

    def test_delete_doc(self):
        with mock.patch.object(builtins, 'input', lambda x: '11-2'):
            assert app_full.delete_doc() == ('11-2', True)
