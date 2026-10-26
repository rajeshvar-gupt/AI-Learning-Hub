import unittest
from ai_hub.evaluate_rag import select_cases,score,verify_bytes


class ExternalRAGTests(unittest.TestCase):
    def test_protocol_and_metric_contract(self):
        dataset={'data':[{'paragraphs':[
            {'context':'A telescope observes distant stars and planets.',
             'qas':[{'id':'a','question':'What observes stars?','answers':[{'text':'telescope'}]}]},
            {'context':'A microscope magnifies small cells.',
             'qas':[{'id':'b','question':'What magnifies cells?','answers':[{'text':'microscope'}]}]}]}]}
        docs,cases=select_cases(dataset);report=score(docs,cases)
        self.assertEqual(report['questions'],2);self.assertEqual(report['document_recall_at_2'],1)
        self.assertEqual([r['id'] for r in report['cases']],['a','b'])
        self.assertNotIn('query',report['cases'][0]);self.assertNotIn('answers',report['cases'][0])

    def test_bad_integrity_and_empty_selection(self):
        with self.assertRaises(ValueError):verify_bytes(b'changed bytes')
        with self.assertRaises(ValueError):select_cases({'data':[]})
