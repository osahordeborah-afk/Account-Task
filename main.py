import pandas as pd
from datetime import datetime

# -----------------------------
# 1. Load accounting data
# -----------------------------

petty_cash = pd.read_csv("petty_cash.csv")
invoices = pd.read_csv("invoices.csv")
purchase_orders = pd.read_csv("purchase_orders.csv")
budget = pd.read_csv("budget.csv")

# -----------------------------
# 2. Petty cash monitoring
# -----------------------------

def analyze_petty_cash(df):
    df["date"] = pd.to_datetime(df["date"])
    df["turnaround_days"] = (
        pd.to_datetime(df["approved_date"]) - pd.to_datetime(df["request_date"])
    ).dt.days

    summary = {
        "total_requests": len(df),
        "total_cash_disbursed": df["amount"].sum(),
        "average_turnaround_days": round(df["turnaround_days"].mean(), 2),
        "pending_requests": len(df[df["status"] == "Pending"])
    }

    return summary


# -----------------------------
# 3. Invoice and purchase order reconciliation
# -----------------------------

def reconcile_invoices(invoices, purchase_orders):
    merged = invoices.merge(
        purchase_orders,
        on="po_number",
        how="left",
        suffixes=("_invoice", "_po")
    )

    merged["amount_match"] = merged["invoice_amount"] == merged["po_amount"]
    merged["vendor_match"] = merged["vendor_invoice"] == merged["vendor_po"]

    exceptions = merged[
        (merged["amount_match"] == False) |
        (merged["vendor_match"] == False) |
        (merged["po_amount"].isna())
    ]

    return merged, exceptions


# -----------------------------
# 4. Budget variance analysis
# -----------------------------

def analyze_budget(budget_df):
    budget_df["variance"] = budget_df["actual_spend"] - budget_df["approved_budget"]
    budget_df["variance_percent"] = (
        budget_df["variance"] / budget_df["approved_budget"]
    ) * 100

    budget_df["status"] = budget_df["variance"].apply(
        lambda x: "Over Budget" if x > 0 else "Within Budget"
    )

    return budget_df


# -----------------------------
# 5. Year-end financial report
# -----------------------------

def generate_year_end_report(petty_cash_summary, reconciled_data, exceptions, budget_analysis):
    report = {
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "petty_cash_summary": petty_cash_summary,
        "total_invoices_processed": len(reconciled_data),
        "invoice_exceptions_found": len(exceptions),
        "total_budgeted_amount": budget_analysis["approved_budget"].sum(),
        "total_actual_spend": budget_analysis["actual_spend"].sum(),
        "total_budget_variance": budget_analysis["variance"].sum()
    }

    return report


# -----------------------------
# 6. Run automation
# -----------------------------

petty_cash_summary = analyze_petty_cash(petty_cash)

reconciled_data, invoice_exceptions = reconcile_invoices(
    invoices,
    purchase_orders
)

budget_analysis = analyze_budget(budget)

year_end_report = generate_year_end_report(
    petty_cash_summary,
    reconciled_data,
    invoice_exceptions,
    budget_analysis
)

# -----------------------------
# 7. Export outputs
# -----------------------------

pd.DataFrame([petty_cash_summary]).to_csv(
    "petty_cash_summary.csv",
    index=False
)

reconciled_data.to_csv(
    "invoice_reconciliation_report.csv",
    index=False
)

invoice_exceptions.to_csv(
    "invoice_exceptions.csv",
    index=False
)

budget_analysis.to_csv(
    "budget_variance_report.csv",
    index=False
)

pd.DataFrame([year_end_report]).to_csv(
    "year_end_financial_summary.csv",
    index=False
)

print("Accounting automation completed successfully.")
print(year_end_report)
