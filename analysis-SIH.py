invoices = [
    {"invoiceId": 1, "items": [["Product1", "2023-01-15", 150, 140], ["Product2", "2023-01-15", 20000, 19000]]},
    {"invoiceId": 2, "items": [["Product3", "2023-01-25", 100, 90], ["Product4", "2023-01-25", 250, 240]]},
    {"invoiceId": 3, "items": [["Product5", "2023-02-10", 300, 290]]},
    {"invoiceId": 4, "items": [["Product6", "2023-02-20", 180, 170], ["Product2", "2023-02-20", 220000, 210000]]},
    {"invoiceId": 5, "items": [["Product8", "2023-03-05", 250, 240], ["Product9", "2023-03-05", 300, 290]]},
    {"invoiceId": 6, "items": [["Product10", "2023-03-15", 350, 340]]},
    {"invoiceId": 7, "items": [["Product11", "2023-04-10", 400, 390], ["Product12", "2023-04-10", 450, 440]]},
    {"invoiceId": 8, "items": [["Product13", "2023-04-20", 500, 490]]},
    {"invoiceId": 9, "items": [["Product14", "2023-05-05", 550, 540], ["Product15", "2023-05-05", 600, 590]]},
    {"invoiceId": 10, "items": [["Product16", "2023-05-15", 650, 640], ["Product17", "2023-05-15", 700, 690]]},
    {"invoiceId": 11, "items": [["Product18", "2023-06-10", 750, 740]]},
    {"invoiceId": 12, "items": [["Product19", "2023-06-20", 800, 790], ["Product20", "2023-06-20", 850, 840]]},
    {"invoiceId": 13, "items": [["Product21", "2023-07-05", 900, 890], ["Product22", "2023-07-05", 950, 940]]},
    {"invoiceId": 14, "items": [["Product23", "2023-07-15", 1000, 990]]},
    {"invoiceId": 15, "items": [["Product24", "2023-08-10", 1050, 1040], ["Product25", "2023-08-10", 1100, 1090]]},
    {"invoiceId": 16, "items": [["Product26", "2023-08-20", 1150, 1140]]},
    {"invoiceId": 17, "items": [["Product27", "2023-09-05", 1200, 1190], ["Product28", "2023-09-05", 1250, 1240]]},
    {"invoiceId": 18, "items": [["Product29", "2023-09-15", 1300, 1290]]},
    {"invoiceId": 19, "items": [["Product30", "2023-10-10", 1350, 1340], ["Product31", "2023-10-10", 1400, 1390]]},
    {"invoiceId": 20, "items": [["Product32", "2023-10-20", 1450, 1440]]},
    {"invoiceId": 21, "items": [["Product33", "2023-11-05", 1500, 1490], ["Product34", "2023-11-05", 1550, 1540]]},
    {"invoiceId": 22, "items": [["Product35", "2023-11-15", 1600, 1590]]},
    {"invoiceId": 23, "items": [["Product36", "2023-12-01", 1650, 1640], ["Product37", "2023-12-01", 1700, 1690]]},
    {"invoiceId": 24, "items": [["Product38", "2023-12-10", 1750, 1740]]},
    {"invoiceId": 25, "items": [["Product39", "2024-01-05", 1800, 1790], ["Product40", "2024-01-05", 1850, 1840]]},
    {"invoiceId": 26, "items": [["Product41", "2024-01-15", 1900, 1890]]},
    {"invoiceId": 27, "items": [["Product42", "2024-02-01", 1950, 1940], ["Product43", "2024-02-01", 2000, 1990]]},
    {"invoiceId": 28, "items": [["Product44", "2024-02-10", 2050, 2040]]},
    {"invoiceId": 29, "items": [["Product45", "2024-03-05", 2100, 2090], ["Product46", "2024-03-05", 2150, 2140]]},
    {"invoiceId": 30, "items": [["Product47", "2024-03-15", 2200, 2190]]},
    {"invoiceId": 31, "items": [["Product48", "2024-04-01", 2250, 2240], ["Product49", "2024-04-01", 2300, 2290]]},
    {"invoiceId": 32, "items": [["Product50", "2024-04-10", 2350, 2340]]},
    {"invoiceId": 33, "items": [["Product51", "2024-05-05", 2400, 2390], ["Product52", "2024-05-05", 2450, 2440]]},
    {"invoiceId": 34, "items": [["Product53", "2024-05-15", 2500, 2490]]},
    {"invoiceId": 35, "items": [["Product54", "2024-06-01", 2550, 2540], ["Product55", "2024-06-01", 2600, 2590]]},
    {"invoiceId": 36, "items": [["Product56", "2024-06-10", 2650, 2640]]},
    {"invoiceId": 37, "items": [["Product57", "2024-07-05", 2700, 2690], ["Product58", "2024-07-05", 2750, 2740]]},
    {"invoiceId": 38, "items": [["Product59", "2024-07-15", 2800, 2790]]},
    {"invoiceId": 39, "items": [["Product60", "2024-08-01", 2850, 2840], ["Product61", "2024-08-01", 2900, 2890]]},
    {"invoiceId": 40, "items": [["Product62", "2024-08-10", 2950, 2940]]},
    {"invoiceId": 41, "items": [["Product63", "2024-09-05", 3000, 2990], ["Product64", "2024-09-05", 3050, 3040]]},
    {"invoiceId": 42, "items": [["Product65", "2024-09-15", 3100, 3090]]},
    {"invoiceId": 43, "items": [["Product66", "2024-10-01", 3150, 3140], ["Product67", "2024-10-01", 3200, 3190]]},
    {"invoiceId": 44, "items": [["Product68", "2024-10-10", 3250, 3240]]},
    {"invoiceId": 45, "items": [["Product69", "2024-11-05", 3300, 3290], ["Product70", "2024-11-05", 3350, 3340]]},
    {"invoiceId": 46, "items": [["Product71", "2024-11-15", 3400, 3390]]},
    {"invoiceId": 47, "items": [["Product72", "2024-12-01", 3450, 3440], ["Product73", "2024-12-01", 3500, 3490]]},
    {"invoiceId": 48, "items": [["Product74", "2024-12-10", 3550, 3540]]},
    {"invoiceId": 49, "items": [["Product75", "2025-01-05", 3600, 3590], ["Product76", "2025-01-05", 3650, 3640]]},
    {"invoiceId": 50, "items": [["Product77", "2025-01-15", 3700, 3690]]},
    {"invoiceId": 51, "items": [["Product78", "2025-02-01", 3750, 3740], ["Product79", "2025-02-01", 3800, 3790]]},
    {"invoiceId": 52, "items": [["Product80", "2025-02-10", 3850, 3840]]},
    {"invoiceId": 53, "items": [["Product81", "2025-03-05", 3900, 3890], ["Product82", "2025-03-05", 3950, 3940]]},
    {"invoiceId": 54, "items": [["Product83", "2025-03-15", 4000, 3990]]},
    {"invoiceId": 55, "items": [["Product84", "2025-04-01", 4050, 4040], ["Product85", "2025-04-01", 4100, 4090]]},
    {"invoiceId": 56, "items": [["Product86", "2025-04-10", 4150, 4140]]},
    {"invoiceId": 57, "items": [["Product87", "2025-05-05", 4200, 4190], ["Product88", "2025-05-05", 4250, 4240]]},
    {"invoiceId": 58, "items": [["Product89", "2025-05-15", 4300, 4290]]},
    {"invoiceId": 59, "items": [["Product90", "2025-06-01", 4350, 4340], ["Product91", "2025-06-01", 4400, 4390]]},
    {"invoiceId": 60, "items": [["Product92", "2025-06-10", 4450, 4440]]},
    {"invoiceId": 61, "items": [["Product93", "2025-07-05", 4500, 4490], ["Product94", "2025-07-05", 4550, 4540]]},
    {"invoiceId": 62, "items": [["Product95", "2025-07-15", 4600, 4590]]},
    {"invoiceId": 63, "items": [["Product96", "2025-08-01", 4650, 4640], ["Product97", "2025-08-01", 4700, 4690]]},
    {"invoiceId": 64, "items": [["Product98", "2025-08-10", 4750, 4740]]},
    {"invoiceId": 65, "items": [["Product99", "2025-09-05", 4800, 4790], ["Product100", "2025-09-05", 4850, 4840]]},
    {"invoiceId": 66, "items": [["Product101", "2025-09-15", 4900, 4890]]},
    {"invoiceId": 67, "items": [["Product102", "2025-10-01", 4950, 4940], ["Product103", "2025-10-01", 5000, 4990]]},
    {"invoiceId": 68, "items": [["Product104", "2025-10-10", 5050, 5040]]},
    {"invoiceId": 69, "items": [["Product105", "2025-11-05", 5100, 5090], ["Product106", "2025-11-05", 5150, 5140]]},
    {"invoiceId": 70, "items": [["Product107", "2025-11-15", 5200, 5190]]},
    {"invoiceId": 71, "items": [["Product108", "2025-12-01", 5250, 5240], ["Product109", "2025-12-01", 5300, 5290]]},
    {"invoiceId": 72, "items": [["Product110", "2025-12-10", 5350, 5340]]},
    {"invoiceId": 73, "items": [["Product111", "2026-01-05", 5400, 5390], ["Product112", "2026-01-05", 5450, 5440]]},
    {"invoiceId": 74, "items": [["Product113", "2026-01-15", 5500, 5490]]},
    {"invoiceId": 75, "items": [["Product114", "2026-02-01", 5550, 5540], ["Product115", "2026-02-01", 5600, 5590]]},
    {"invoiceId": 76, "items": [["Product116", "2026-02-10", 5650, 5640]]},
    {"invoiceId": 77, "items": [["Product117", "2026-03-05", 5700, 5690], ["Product118", "2026-03-05", 5750, 5740]]},
    {"invoiceId": 78, "items": [["Product119", "2026-03-15", 5800, 5790]]},
    {"invoiceId": 79, "items": [["Product120", "2026-04-01", 5850, 5840], ["Product121", "2026-04-01", 5900, 5890]]},
    {"invoiceId": 80, "items": [["Product122", "2026-04-10", 5950, 5940]]},
    {"invoiceId": 81, "items": [["Product123", "2026-05-05", 6000, 5990], ["Product124", "2026-05-05", 6050, 6040]]},
    {"invoiceId": 82, "items": [["Product125", "2026-05-15", 6100, 6090]]},
    {"invoiceId": 83, "items": [["Product126", "2026-06-01", 6150, 6140], ["Product127", "2026-06-01", 6200, 6190]]},
    {"invoiceId": 84, "items": [["Product128", "2026-06-10", 6250, 6240]]},
    {"invoiceId": 85, "items": [["Product129", "2026-07-05", 6300, 6290], ["Product130", "2026-07-05", 6350, 6340]]},
    {"invoiceId": 86, "items": [["Product131", "2026-07-15", 6400, 6390]]},
    {"invoiceId": 87, "items": [["Product132", "2026-08-01", 6450, 6440], ["Product133", "2026-08-01", 6500, 6490]]},
    {"invoiceId": 88, "items": [["Product134", "2026-08-10", 6550, 6540]]},
    {"invoiceId": 89, "items": [["Product135", "2026-09-05", 6600, 6590], ["Product136", "2026-09-05", 6650, 6640]]},
    {"invoiceId": 90, "items": [["Product137", "2026-09-15", 6700, 6690]]},
    {"invoiceId": 91, "items": [["Product138", "2026-10-01", 6750, 6740], ["Product139", "2026-10-01", 6800, 6790]]},
    {"invoiceId": 92, "items": [["Product140", "2026-10-10", 6850, 6840]]},
    {"invoiceId": 93, "items": [["Product141", "2026-11-05", 6900, 6890], ["Product142", "2026-11-05", 6950, 6940]]},
    {"invoiceId": 94, "items": [["Product143", "2026-11-15", 7000, 6990]]},
    {"invoiceId": 95, "items": [["Product144", "2026-12-01", 7050, 7040], ["Product145", "2026-12-01", 7100, 7090]]},
    {"invoiceId": 96, "items": [["Product146", "2026-12-10", 7150, 7140]]},
    {"invoiceId": 97, "items": [["Product147", "2027-01-05", 7200, 7190], ["Product148", "2027-01-05", 7250, 7240]]},
    {"invoiceId": 98, "items": [["Product149", "2027-01-15", 7300, 7290]]},
    {"invoiceId": 99, "items": [["Product150", "2027-02-01", 7350, 7340], ["Product151", "2027-02-01", 7400, 7390]]},
    {"invoiceId": 100, "items": [["Product152", "2027-02-10", 7450, 7440]]}
]

import pandas as pd
import matplotlib.pyplot as plt

def calculate_sales_overview(invoices):
    total_revenue = 0
    total_invoices = len(invoices)
    total_units_sold = 0

    for invoice in invoices:
        for item in invoice['items']:
            product_name, date, mrp, price = item
            total_revenue += price
            total_units_sold += 1 
    average_order_value = total_revenue / total_invoices if total_invoices > 0 else 0

    return {
        "Total Revenue": total_revenue,
        "Total Number of Invoices": total_invoices,
        "Average Order Value": average_order_value,
        "Total Units Sold": total_units_sold
    }

# Example usage
sales_overview = calculate_sales_overview(invoices) 
# returns a dictionary with the following key-value pairs
#  "Total Revenue": ,
#  "Total Number of Invoices": ,
#  "Average Order Value": ,
#  "Total Units Sold": 
print(sales_overview)




def prepare_sales_data(invoices):
    data = []
    for invoice in invoices:
        for item in invoice['items']:
            product_name, date, mrp, price = item
            data.append({"date": date, "price": price, "invoiceId": invoice['invoiceId']})
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    return df

def plot_sales_over_time(df, frequency='M'):
    sales_over_time = df.resample(frequency, on='date')['price'].sum()
    avg_sales = sales_over_time.mean()

    plt.figure(figsize=(12, 8))
    plt.plot(sales_over_time.index, sales_over_time.values, marker='o', linestyle='-', color='#1f77b4', linewidth=2)
    plt.axhline(y=avg_sales, color='red', linestyle='--', linewidth=2, label=f'Average Sales ({frequency})')
    plt.title(f"Sales Over Time (Aggregated by {frequency})", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Total Sales", fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_invoice_count_over_time(df, frequency='M'):
    invoice_count_over_time = df.resample(frequency, on='date')['invoiceId'].nunique()
    avg_invoices = invoice_count_over_time.mean()

    plt.figure(figsize=(14, 8))
    bars = plt.bar(invoice_count_over_time.index, invoice_count_over_time.values, color='#ff7f0e', edgecolor='black')
    
    # Add annotations
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', ha='center', fontsize=10, color='black')

    plt.axhline(y=avg_invoices, color='blue', linestyle='--', linewidth=2, label=f'Average Invoices ({frequency})')
    plt.title(f"Invoice Count Over Time (Aggregated by {frequency})", fontsize=18)
    plt.xlabel("Date", fontsize=16)
    plt.ylabel("Number of Invoices", fontsize=16)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7, which='both', axis='y')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Example usage
df = prepare_sales_data(invoices)

# Plot sales over time aggregated by month ('M')
plot_sales_over_time(df, frequency='M')

# Plot invoice count over time aggregated by month ('M')
plot_invoice_count_over_time(df, frequency='M')

# Plot sales over time aggregated by week ('W')
plot_sales_over_time(df, frequency='W')

# Plot invoice count over time aggregated by week ('W')
plot_invoice_count_over_time(df, frequency='W')

# Plot sales over time aggregated by day ('D')
plot_sales_over_time(df, frequency='D')

# Plot invoice count over time aggregated by day ('D')
plot_invoice_count_over_time(df, frequency='D')





def prepare_discount_data(invoices):
    data = []
    for invoice in invoices:
        for item in invoice['items']:
            product_name, date, mrp, price = item
            discount = ((mrp - price) / mrp )* 100
            data.append({"date": date, "price": price, "invoiceId": invoice['invoiceId'], "discount": discount})
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    return df

def plot_discount_trends(df, frequency='M'):
    # Calculate discount trends
    discount_over_time = df.resample(frequency, on='date')['discount'].mean()
    avg_discount = discount_over_time.mean()

    plt.figure(figsize=(12, 8))
    plt.plot(discount_over_time.index, discount_over_time.values, marker='o', linestyle='-', color='#2ca02c', linewidth=2)
    plt.axhline(y=avg_discount, color='red', linestyle='--', linewidth=2, label=f'Average Discount ({frequency})')
    plt.title(f"Discount Trends Over Time (Aggregated by {frequency})", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Average Discount", fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage
df = prepare_discount_data(invoices)

# Plot discount trends aggregated by month ('M')
plot_discount_trends(df, frequency='M')

# Plot discount trends aggregated by week ('W')
plot_discount_trends(df, frequency='W')

# Plot discount trends aggregated by day ('D')
plot_discount_trends(df, frequency='D')




def prepare_product_revenue_data(invoices):
    data = []
    for invoice in invoices:
        for item in invoice['items']:
            product_name, date, mrp, price = item
            data.append({"product_name": product_name, "price": price})
    
    df = pd.DataFrame(data)
    return df

def plot_top_products_by_revenue(df):
    # Aggregate revenue by product
    product_revenue = df.groupby('product_name')['price'].sum().reset_index()
    
    # Sort products by revenue in descending order
    top_products = product_revenue.sort_values(by='price', ascending=False).head(10)
    
    plt.figure(figsize=(14, 8))
    bars = plt.bar(top_products['product_name'], top_products['price'], color='#1f77b4', edgecolor='black')
    
    # Add annotations
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:,.2f}', va='bottom', ha='center', fontsize=10, color='black')

    plt.title("Top 10 Selling Products by Revenue", fontsize=18)
    plt.xlabel("Product Name", fontsize=16)
    plt.ylabel("Total Revenue", fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, linestyle='--', alpha=0.7, which='both', axis='y')
    plt.tight_layout()
    plt.show()

# Example usage
df = prepare_product_revenue_data(invoices)
plot_top_products_by_revenue(df)





