from google.cloud import bigquery
print("BigQuery client library imported successfully.")

def query_public_dataset():
    # Create a BigQuery client
    client = bigquery.Client()
    print("BigQuery client created successfully.")

    # Define the SQL query to retrieve data from a public dataset
    query = """
    select order_items.id, product_id, products.name 
    from `bigquery-public-data.thelook_ecommerce.order_items` as order_items
    left join `bigquery-public-data.thelook_ecommerce.products` as products
    on order_items.product_id=products.id
    limit 100
    """
    print("Executing query...")

    #for row in client.query(query).result():  # Execute the query and iterate over the results
    #    print(f"{row}")   

    results = client.query(query).to_dataframe()[:100]  # Execute the query and convert the results to a DataFrame
    print(results)  # Print the first 5 rows of the results

    
if __name__ == "__main__":
    query_public_dataset()