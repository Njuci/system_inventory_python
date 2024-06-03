import json

data_list = ["élément1", "élément2", "élément3"]
data_string = json.dumps(data_list)
import mysql.connector
import json

def save_list_to_mysql(data_list, table_name, text_column):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="3670njci",
        database="bd_test"
    )

    data_string = json.dumps(data_list)
    cursor = db.cursor()
    sql = f"INSERT INTO {table_name} ({text_column}) VALUES (%s)"
    cursor.execute(sql, (data_string,))
    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    data_list = ["élément1", "élément2", "élément3"]
    table_name = "tb_test"
    text_column = "liste"

    save_list_to_mysql(data_list, table_name, text_column)
