"""Contracts, edge cases and evaluation invariants for the offline labs."""
import importlib.util
from pathlib import Path
import unittest
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def module(folder, filename):
    path = ROOT / "projects" / "intermediate" / folder / filename
    spec = importlib.util.spec_from_file_location(folder.replace("-", "_"), path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


foundation = module("foundations-lab", "foundations.py")
sales = module("sales-analysis", "sales.py")
train = module("supervised-ml", "train.py")
books = module("book-recommender", "recommend.py")
explore = module("unsupervised-ml", "explore.py")


class FoundationsTests(unittest.TestCase):
    def test_converges_and_descends(self):
        w, losses = foundation.gradient_descent()
        self.assertAlmostEqual(w, 3, places=7)
        self.assertTrue(all(b <= a for a, b in zip(losses, losses[1:])))

    def test_invalid_optimizer_inputs(self):
        for args in [dict(rate=0), dict(rate=1), dict(start=float("nan")), dict(steps=0), dict(steps=True)]:
            with self.assertRaises(ValueError):
                foundation.gradient_descent(**args)

    def test_known_statistics(self):
        report = foundation.summarize([2, 4, 4, 6], null_mean=4)
        self.assertEqual(report["mean"], 4)
        self.assertAlmostEqual(report["sample_sd"], np.sqrt(8/3))
        self.assertEqual(report["p"], 1)
        self.assertLess(report["mean_ci95"][0], 4)
        self.assertGreater(report["mean_ci95"][1], 4)

    def test_invalid_statistics(self):
        for values in [[], [1], [2, 2], [1, np.inf], [[1, 2], [3, 4]]]:
            with self.assertRaises(ValueError):
                foundation.summarize(values)


class SalesTests(unittest.TestCase):
    def test_expected_totals_and_audit(self):
        summary, audit = sales.analyze(*sales.fixture())
        self.assertEqual(summary.to_dict(), {"books": 100., "courses": 90.})
        self.assertEqual(audit["valid_orders"], 5)
        self.assertEqual(audit["exact_duplicates_removed"], 1)
        self.assertEqual(audit["rejected_order_ids"], [6, 7])
        self.assertEqual(audit["total_revenue"], 190)

    def test_unknown_product_rejected(self):
        orders, products = sales.fixture()
        orders.loc[0, "product_id"] = "absent"
        with self.assertRaises(ValueError):
            sales.analyze(orders, products)

    def test_join_multiplication_rejected(self):
        orders, products = sales.fixture()
        products = pd.concat([products, products.iloc[[0]]])
        with self.assertRaises(pd.errors.MergeError):
            sales.analyze(orders, products)

    def test_conflicting_order_rejected(self):
        orders, products = sales.fixture()
        orders.loc[1, "order_id"] = 1
        with self.assertRaises(ValueError):
            sales.analyze(orders, products)

    def test_bad_numeric_row_rejected(self):
        orders, products = sales.fixture()
        orders.loc[0, "quantity"] = np.inf
        _, audit = sales.analyze(orders, products)
        self.assertIn(1, audit["rejected_order_ids"])


class ModelTests(unittest.TestCase):
    def test_split_disjoint(self):
        for data in [train.regression_data(), train.classification_data()]:
            X_train, X_test, _, _ = data
            self.assertFalse(set(map(tuple, X_train)) & set(map(tuple, X_test)))

    def test_scaler_only_learns_training_mean(self):
        X = np.array([[0., 1.], [2., 3.], [4., 5.]])
        model = train.pipeline(train.Ridge()).fit(X, [0, 1, 2])
        before = model.named_steps["scale"].mean_.copy()
        model.predict([[1000., 1001.]])
        np.testing.assert_allclose(before, X.mean(axis=0))
        np.testing.assert_allclose(model.named_steps["scale"].mean_, before)

    def test_holdout_reports(self):
        for task in ["regression", "classification"]:
            report = train.evaluate(task)
            self.assertEqual(report["cv_folds"], 5)
            self.assertIn(report["selected"], [r["name"] for r in report["candidates"]])
            if task == "regression":
                self.assertLess(report["selected_test"]["mae"], report["baseline_test"]["mae"])
            else:
                self.assertEqual(np.array(report["selected_test"]["confusion_matrix"]).sum(), report["test_rows"])
                self.assertGreater(report["selected_test"]["macro_f1"], report["baseline_test"]["macro_f1"])

    def test_clustering_contract(self):
        report, points, labels = explore.explore()
        self.assertEqual(points.shape, (240, 2))
        self.assertEqual(sum(report["cluster_sizes"]), len(labels))
        self.assertTrue(-1 <= report["silhouette"] <= 1)
        self.assertLessEqual(sum(report["explained_variance_ratio"]), 1 + 1e-12)


class RecommendationTests(unittest.TestCase):
    def test_no_self_and_order(self):
        result = books.recommend("python")
        self.assertNotIn("python", [r["id"] for r in result])
        self.assertEqual(len({r["id"] for r in result}), len(result))
        scores = [r["similarity"] for r in result]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertTrue(all(0 < s <= 1 + 1e-12 for s in scores))

    def test_no_overlap_is_empty(self):
        self.assertEqual(books.recommend("garden"), [])

    def test_invalid_requests(self):
        for id, k in [("missing", 3), ("python", 0), ("python", True)]:
            with self.assertRaises(ValueError):
                books.recommend(id, k)

    def test_duplicate_ids(self):
        with self.assertRaises(ValueError):
            books.recommend("python", books=[books.BOOKS[0], books.BOOKS[0]])


if __name__ == "__main__":
    unittest.main()
