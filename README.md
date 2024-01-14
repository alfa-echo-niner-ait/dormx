# DormX

_DormX_ is a simple web application for buying and selling, specifically designed for students residing in the university dormitory area. The platform enables students to easily exchange their used or unnecessary items, as well as inquire about products within a specified price range. In both buying and selling scenarios, users can submit competitive bids. Subsequently, the product owner can access the bidder's contact information to facilitate the completion of the transaction. Our primary focus is on efficiently and effectively implementing the use of a _Relational Database Management System (RDBMS)_ in a real-life scenario. We have established relationships between entities and normalized our database to cater to the requirements, ensuring its seamless functionality in various _CRUD (Create, Read, Update, Delete)_ operations.


### A Group Project by

- __Ayub Ali Emon__, Student ID: 202001051911, Email: aaemon98@163.com
- __Phonesamay Phoutthavong__, Student ID: 202001061406, Email: phphonesamay@gmail.com

`Students of Software Engineering 2020(International Students)`


### Project Assigned by

- __Dr. QianQian Li__, Email: sdnuliqian@163.com, Computer Science and Information Department

__`Shandong Univerity of Science and Technology`__


### Project Tools

- Python 3.12.1
- Python's Flask as Backend
- Bootstrap 5 for frontend
- MySQL as Database

### How to Setup?

1. Install the necessary packages from `requirements.txt` or install them manually one by one.
  ```
  pip install -r requirements.txt
  ```
2. Set up your MySQL database.
   
   First, create the database, then import `dormx_db.sql` if you want only tables. But if you want tables along with sample data, import `dormx_data.sql`
   Or you can manually create the tables and modify them as you need. Here is the database relationship structure.
   
   <img src="https://github.com/alfa-echo-niner-ait/dormx/assets/78315132/d3c47119-020c-4bf5-9a0f-3ba5bdf811e3" alt="DormX Database" />

3. Modify your database information in `src/__init__.py` file. Change __SECRET_KEY__, __DB_NAME__, __DB_USERNAME__, __DB_PASSWORD__
4. Then you can run the `run.py` file to start the server. Debug mode is set to true, set false if you don't need.

