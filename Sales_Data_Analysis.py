# Mini Project 2: Advanced Sales Data Analysis

# Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def list_operations():
    print("=== List Operations ===")
    sales_amounts = [250, 450, 300, 700, 150]
    print("Original sales:", sales_amounts)

    # Append new sale
    sales_amounts.append(500)
    print("After appending 500:", sales_amounts)

    # Remove a sale
    sales_amounts.remove(300)
    print("After removing 300:", sales_amounts)

    # Sort sales
    sales_amounts.sort()
    print("Sorted sales:", sales_amounts)
    return sales_amounts

def tuple_and_set_operations():
    print("\n=== Tuples and Sets ===")
    product_categories = ("Electronics", "Clothing", "Groceries")
    print("Product categories (tuple):", product_categories)

    store_a_products = {"TV", "Shirt", "Apple", "Laptop"}
    store_b_products = {"Laptop", "Shirt", "Banana", "Tablet"}

    all_products = store_a_products.union(store_b_products)
    print("Union of products:", all_products)

    common_products = store_a_products.intersection(store_b_products)
    print("Intersection of products:", common_products)

    only_in_a = store_a_products.difference(store_b_products)
    print("Products only in Store A:", only_in_a)

def dictionary_operations():
    print("\n=== Dictionary Operations ===")
    product_sales = {
        "TV": 120,
        "Shirt": 250,
        "Apple": 180,
        "Laptop": 90,
        "Banana": 130
    }

    print("Initial product sales:", product_sales)

    # Add new product
    product_sales["Tablet"] = 60

    # Update sales
    product_sales["Apple"] += 20

    print("Updated product sales:", product_sales)
    return product_sales

def numpy_operations(sales_list):
    print("\n=== NumPy Operations ===")
    sales_np = np.array(sales_list)
    total_sales = np.sum(sales_np)
    average_sales = np.mean(sales_np)
    print(f"Total sales: {total_sales}")
    print(f"Average sales: {average_sales:.2f}")
    return sales_np

def pandas_operations(product_sales):
    print("\n=== Pandas Operations ===")
    data = {
        "Product": list(product_sales.keys()),
        "Units Sold": list(product_sales.values()),
        "Price": [500, 30, 1, 1200, 0.5, 350]  # Example prices aligned with products
    }
    df = pd.DataFrame(data)
    print("Initial DataFrame:\n", df)

    df["Revenue"] = df["Price"] * df["Units Sold"]
    print("\nDataFrame with Revenue:\n", df)

    df_sorted = df.sort_values(by="Revenue", ascending=False)
    print("\nDataFrame sorted by Revenue:\n", df_sorted)

    high_revenue = df[df["Revenue"] > 5000]
    print("\nProducts with revenue > 5000:\n", high_revenue)
    return df

def visualize_data(df):
    print("\n=== Data Visualization ===")
    # Barplot: Units Sold
    plt.figure(figsize=(8,5))
    sns.barplot(x="Product", y="Units Sold", data=df)
    plt.title("Units Sold by Product")
    plt.show()

    # Plotly line graph: Revenue by Product
    fig = px.line(df, x="Product", y="Revenue", title="Revenue by Product", markers=True)
    fig.show()

    # Heatmap of correlations (numeric only)
    plt.figure(figsize=(6,4))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()


def sql_like_operations(df):
    print("\n=== SQL-like Operations with Pandas ===")
    selected_data = df[["Product", "Revenue"]]
    print("\nSelected Columns:\n", selected_data)

    electronics = df[df["Product"].isin(["TV", "Laptop", "Tablet"])]
    print("\nFilter Electronics Products:\n", electronics)

    revenue_by_category = {
        "Electronics": electronics["Revenue"].sum(),
        "Others": df[~df["Product"].isin(["TV", "Laptop", "Tablet"])]["Revenue"].sum()
    }
    print("\nRevenue by Category (Simulated):\n", revenue_by_category)

def main():
    sales_list = list_operations()
    tuple_and_set_operations()
    product_sales = dictionary_operations()
    sales_np = numpy_operations(sales_list)
    df = pandas_operations(product_sales)
    visualize_data(df)
    sql_like_operations(df)

if __name__ == "__main__":
    main()