DROP TABLE IF EXISTS Salesperson CASCADE;
CREATE TABLE Salesperson (
    ID int,
    Name varchar(255),
    Age int,
    Salary int,
    PRIMARY KEY (ID),
    UNIQUE(ID)
 );

DROP TABLE IF EXISTS Customer CASCADE;
CREATE TABLE Customer (
  ID int,
  Name varchar(255),
  City varchar(255),
  Industry_Type varchar(255),
  PRIMARY KEY (ID),
  UNIQUE (ID)
);

DROP TABLE IF EXISTS Orders CASCADE;
CREATE TABLE Orders (

  Number int,
  order_date varchar(255),
  cust_id int,
  salesperson_id int,
  Amount int,
  CONSTRAINT fk_cust_id FOREIGN KEY (cust_id) REFERENCES Customer (ID),
  CONSTRAINT fk_salesperson_id FOREIGN KEY (salesperson_id) REFERENCES Salesperson (ID)
);


INSERT INTO Customer
  (ID, Name, City, Industry_Type)
VALUES
  (4, 'Samsonic', 'pleasant','J'),
  (6, 'Panasung', 'oaktown','J'),
  (7, 'Samony', 'jackson', 'B'),
  (9, 'Orange', 'Jackson', 'B');

INSERT INTO Salesperson
  (ID, Name, Age, Salary)
VALUES
  (1,'Abe',61,140000),
  (2,'Bob',34,44000),
  (5,'Chris',34,40000),
  (7,'Dan',41,52000),
  (8,'Ken',57,115000),
  (11,'Joe',38,38000);


INSERT INTO Orders
  (Number, order_date, cust_id, salesperson_id, Amount)
VALUES
  (10, '8/2/96', 4, 2, 540),
  (20, '1/30/99', 4, 8, 1800),
  (30, '7/14/95', 9, 1, 460),
  (40, '1/29/98', 7, 2, 2400),
  (50, '2/3/98', 6, 7, 600),
  (60, '3/2/98', 6, 7, 720),
  (70, '5/6/98', 9, 7, 150);

