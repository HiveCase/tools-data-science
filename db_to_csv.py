import sqlite3
import pandas as pd
import os

# Function to convert SQLite table to CSV
def db_to_csv(db_name, table_name, csv_path):
    try:
        # Construct the full path to the database file
        db_path = os.path.join(db_name)
        
        # Check if the database file exists
        if not os.path.isfile(db_path):
            print(f"Database file '{db_path}' not found.")
            return
        
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(db_path)
        
        # Read the SQLite table into a pandas DataFrame
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        # Close the connection
        conn.close()
        
        # Export the DataFrame to a CSV file
        df.to_csv(csv_path, index=False)
        
        print(f"Table '{table_name}' has been successfully exported to {csv_path}")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    db_name = "your_database.db"  # Name of your SQLite database file
    table_name = "your_table_name"  # Name of the table you want to export
    csv_path = "output.csv"  # Desired path for the CSV output
    
    db_to_csv(db_name, table_name, csv_path)
