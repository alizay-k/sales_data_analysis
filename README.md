# Sales Data Analysis Project

This is a data analysis project using a realistic sales dataset. It demonstrates **data cleaning, feature engineering, exploratory analysis, and visualizations**.

## Dataset

The dataset (`cleaned_dataset.csv`) contains sales orders with the following columns:

- `order_id` / `serial_no`: Unique order identifier
- `order_date`: Date of the order
- `product`: Product name
- `category`: Product category
- `region`: Sales region
- `quantity`: Quantity sold
- `unit_price`: Price per unit
- `revenue`: Total revenue
- `price_per_unit`: Calculated column (revenue / quantity)
- `order_month`: Extracted month from `order_date`
- `high_value_order`: True if revenue > 1000

## Steps Performed

1. **Data Cleaning**
   - Converted `order_date` to datetime
   - Handled missing `quantity` and `revenue`
   - Dropped unnecessary columns
   - Renamed columns for clarity

2. **Feature Engineering**
   - Calculated `price_per_unit`
   - Extracted `order_month` from `order_date`
   - Flagged `high_value_order` for revenue > 1000

3. **Analysis**
   - Total revenue per region and category
   - Top 3 products by revenue
   - Average order value
   - Region with the highest Electronics sales

4. **Visualizations**
   - Bar charts for revenue by region and category
   - Top 3 products by revenue
   - High value orders per month

## How to Run

1. Make sure you have Python 3.x installed.
2. Install required libraries:

```bash
pip install pandas matplotlib
