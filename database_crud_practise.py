"""
This script Performing crud operation on table name employee.Employee has 7 column field
Employee Id(Auto-Incremental),FirstName,LastName,Email,PhoneNumber,Department,Salary.
"""
import mysql.connector
from mysql.connector import Error
import logging

logger = logging.getLogger("mysql_log")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('my_sql.log', 'w')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#insert data into table
def insert_employee_data(connection, FirstName,LastName,Email,PhoneNumber,Department,Salary):
    """
    :param connection:
    :param FirstName:
    :param LastName:
    :param Email:
    :param PhoneNumber:
    :param Department:
    :param Salary:
    :return:
    """
    if connection.is_connected():
            my_cursor = connection.cursor()
            my_cursor.execute(f"""
                       insert into Employee (FirstName, LastName, Email, PhoneNumber, Department, Salary) 
                       values ('{FirstName}','{LastName}','{Email}','{PhoneNumber}','{Department}',{Salary})
                       """)
            connection.commit()
            logger.info(f"Record inserted successfully")

#reading employee data
def read_employee_data(connection):
    """
    Fetching all the data from the database for 'users' table.
    :param connection:
    :return:
    """
    if connection.is_connected():
            my_cursor = connection.cursor()
            my_cursor.execute("SELECT * FROM Employee;")
            data = my_cursor.fetchall()
            for information in data:
                print(information)
    print()

#read one employee data
def read_one_employee_data(connection,FirstName):
    """
    Fetching only records of the particular person from the 'users' table.
    :param connection:
    :param FirstName:
    :return:
    """
    if connection.is_connected():
            my_cursor=connection.cursor()
            my_cursor.execute(f"SELECT EmployeeID FROM users WHERE name='{FirstName}';")
            result = list(my_cursor.fetchone())
            print(result)
    print()
    return result[0]

#update employee data
def update_employee_data(connection, FirstName):
    """
    Updating record of already available data by fetching it from the database.
    :param connection:
    :param FirstName:
    :return:
    """
    if connection.is_connected():
        id_no = read_one_employee_data(connection, FirstName)
        FirstName = input("Enter the new FirstName : ")
        LastName = input("Enter the new LastName : ")
        Email = input("Enter the new Email : ")
        PhoneNumber = input("Enter the new PhoneNumber : ")
        Department = input("Enter the new Department : ")
        Salary = input("Enter the new Salary : ")
        my_cursor=connection.cursor()
        my_cursor.execute(f"UPDATE users SET Firstname='{FirstName}',LastName='{LastName}, Email='{Email}',PhoneNumber='{PhoneNumber},Department='{Department}',Salary='{Salary}' WHERE id={id_no};")
        connection.commit()
        logger.info(f"Record updated successfully")

#delete employee data
def delete_employee_data(connection, Firstname):
    """
    Deleting a record of particular user_name from the database by fetching it's id.
    :param connection:
    :param Firstname:
    :return:
    """
    if connection.is_connected():
        id_no = read_one_employee_data(connection, Firstname)
        my_cursor=connection.cursor()
        my_cursor.execute(f"DELETE FROM users WHERE id={id_no};")
        connection.commit()
        logger.info("Record deleted successfully from database.")


if __name__ == "__main__":
    connection = mysql.connector.connect(
        host='localhost',
        user="dhruv",
        password="Soft@123",
        database="Employee"
    )
    try:
        while True:
            print("Available operations for database:"
                  "\n1. Insert data"
                  "\n2. Update data"
                  "\n3. Read data"
                  "\n4. Delete data")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                logger.info(f"Insert operation is started:")
                FirstName = input("Enter the new FirstName : ")
                LastName = input("Enter the new LastName : ")
                Email = input("Enter the new Email : ")
                PhoneNumber = input("Enter the new PhoneNumber : ")
                Department = input("Enter the new Department : ")
                Salary = input("Enter the new Salary : ")
                insert_employee_data(connection, FirstName, LastName,Email,PhoneNumber,Department,Salary)
            elif choice == 2:
                logger.info(f"Update operation is on going:")
                username = input("Enter the name: ")
                update_employee_data(connection, username)
            elif choice == 3:
                logger.info(f"Reading operation is started: ")
                read_employee_data(connection)
            elif choice == 4:
                logger.info(f"Deleting operation is started: ")
                name = input("Enter the Firstname: ")
                delete_employee_data(connection, name)
            else:
                logger.info("Quiting from the program :")
                break
    except Error as e:
        logger.error("Something went wrong")
    finally:
        if connection.is_connected():
            connection.close()
            logger.info("MySQL connection is closed")
