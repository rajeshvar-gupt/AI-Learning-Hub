"""Auditable cleaning, pandas/SQLite agreement, and an offline chart."""
import json
import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def fixture():
    orders = pd.DataFrame([
        [1, "p1", 2, 10], [2, "p2", 1, 30], [3, "p1", 3, 10],
        [4, "p3", 2, 25], [5, "p2", 2, 30], [5, "p2", 2, 30],
        [6, "p1", None, 10], [7, "p3", -1, 25],
    ], columns=["order_id", "product_id", "quantity", "unit_price"])
    products = pd.DataFrame([["p1", "books"], ["p2", "courses"], ["p3", "books"]],
                            columns=["product_id", "category"])
    return orders, products


def analyze(orders, products):
    required = {"order_id", "product_id", "quantity", "unit_price"}
    if not required.issubset(orders.columns) or not {"product_id", "category"}.issubset(products.columns):
        raise ValueError("missing required columns")
    clean = orders.drop_duplicates().copy()
    duplicates = len(orders) - len(clean)
    if clean.order_id.isna().any() or clean.order_id.duplicated().any():
        raise ValueError("order IDs must be present and unique after exact deduplication")
    for column in ["quantity", "unit_price"]:
        clean[column] = pd.to_numeric(clean[column], errors="coerce")
    import numpy as np
    valid = (np.isfinite(clean.quantity) & np.isfinite(clean.unit_price)
             & (clean.quantity > 0) & (clean.unit_price >= 0))
    rejected_ids = clean.loc[~valid, "order_id"].tolist()
    clean = clean.loc[valid].copy()
    if clean.empty:
        raise ValueError("no valid orders")
    if products.product_id.isna().any() or products.category.isna().any():
        raise ValueError("product IDs and categories must be present")
    joined = clean.merge(products, on="product_id", how="left", validate="many_to_one", indicator=True)
    if not joined._merge.eq("both").all():
        raise ValueError("unknown product ID")
    joined["revenue"] = joined.quantity * joined.unit_price
    if not np.isfinite(joined.revenue).all():
        raise ValueError("revenue overflow")
    pandas_summary = joined.groupby("category").revenue.sum().sort_index()
    with sqlite3.connect(":memory:") as connection:
        clean.to_sql("orders", connection, index=False)
        products.to_sql("products", connection, index=False)
        sql_summary = pd.read_sql_query("""
            SELECT p.category, SUM(o.quantity*o.unit_price) AS revenue
            FROM orders o JOIN products p ON o.product_id=p.product_id
            GROUP BY p.category ORDER BY p.category
        """, connection).set_index("category").revenue
    pd.testing.assert_series_equal(pandas_summary, sql_summary, check_dtype=False)
    if not np.isclose(pandas_summary.sum(), joined.revenue.sum()):
        raise AssertionError("aggregation changed total revenue")
    audit = dict(input_rows=len(orders), exact_duplicates_removed=duplicates,
                 rejected_order_ids=rejected_ids, valid_orders=len(clean),
                 total_revenue=float(joined.revenue.sum()))
    return pandas_summary, audit


def main(output_dir=None):
    output = Path(output_dir) if output_dir else Path(__file__).parent / "outputs"
    output.mkdir(parents=True, exist_ok=True)
    summary, audit = analyze(*fixture())
    summary.to_csv(output / "category-revenue.csv")
    fig, ax = plt.subplots(figsize=(6, 4))
    summary.plot.bar(ax=ax, color=["#2563eb", "#0d9488"], rot=0)
    ax.set(title="Revenue by category — invented sample", xlabel="Category", ylabel="Revenue (demo units)")
    ax.set_ylim(bottom=0)
    fig.tight_layout()
    fig.savefig(output / "revenue.png", dpi=150)
    plt.close(fig)
    (output / "audit.json").write_text(json.dumps(audit, indent=2), encoding="utf-8")
    print(json.dumps(dict(audit=audit, revenue=summary.to_dict()), indent=2))


if __name__ == "__main__":
    main()
