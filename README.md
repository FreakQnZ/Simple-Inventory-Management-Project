
# Simple-Inventory-Management-Project

Inventory Management Using python programming language and MySQL database.




## Documentation

### List

We have the Materials that are being traded in the store. There is a provision to add new materials. This gets stored in the database.
The Store gets its supplies from various Suppliers. This Supplier list also can be added and is stored in the database.
The Customer is also stored in the list. We have provision to add new Customers which is again stored in the database.
The above 3 Lists –
1.	Material Type
2.	Supplier  
3.	Customer
are used for selecting data.

### Daily Transactions

There are 2 types of processes-
1.	Inward
2.	Outward

When a Material Type is brought into the Store, an Inward operation is performed. For Inward, entry of the following is done-
1.	Supplier (Selection)
2.	Material Type (Selection)
3.	Quantity in Kgs

When a Material Type is taken out of the Store, an Outward operation is performed. For Outward, entry of the following is done – 
1.	Customer (Selection)
2.	Material Type (Selection)
3.	Quantity in Kgs 
For both Inward and Outward, values are stored in the database. For Inward Process, the quantity of corresponding Material gets added up and for outward it gets subtracted.

### Reports

Reports can be obtained after the transactions are made. Reports available are –
1. List of all items.
2. Total inward processes
3. Total outward processes
4. Current Stock






## Deployment

To deploy this project there are 2 steps
1. creation of database and tables.
3. Downloading MySQL python connector.
2. Running python code.

### creation of database and tables.

first we need to login to our MySQL in command line

to do this we open cmd locate MySQL directory then run commans

```bash
  mysql -u [username] -p
```
then we can run the code snippts in text file dbms.txt

### Downloading MySQL python connector.
We need to download python connector for MySQL to access it through our python program. The following link should contain the connector
https://downloads.mysql.com/archives/c-python/

### Running Python code

Here, we just need to run the python code with 1 small change
we need to replace username and password of MySQL with our machine's MySQL credentials [line 59]
## Software versions.

##### MySQL - 8.0.34
##### MySQL Connector - 8.0.33 
##### Python - 3.11.4

