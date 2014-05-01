-- (c) 2014. CSR Development, Co.
-- All rights reserved.
-- MIT License 

-- billing - postgreSQL version
-- mongodb or couchdb version

-- drop database if exists billing;
-- create database billing;
-- use billing;

-- SET datestyle ISO

drop table if exists invoice;
create type invoice_term as enum('Net30', 'Net60', 'Net90', 'OnReceipt');
-- pre and post billing
create table tbl_invoices
(
  invoice_id                int not null,
  invoice_number            int not null, -- todo: unique constraint, sequence i.e., oracle
  invoice_date              date not null, -- ISO ISO 8601/SQL standard 1997-12-17 07:37:16-08
  po_number                 varchar(100), -- purchase order number
  client_id                 int not null,
  terms                     invoice_term,
  tax_exempt                boolean,
  paid                      boolean,
  date_printed              date,
  date_created              date not null,
  user_created              int not null,
  date_modified             date not null,
  user_modified             int not null,
  primary key (invoice_id)
  -- purpose                   varchar(20),
  -- client_billing_address_id int not null,
);

--drop table if exists invoice_line_items;
--create table invoice_line_items
drop table if exists transactions;
create type transaction_type as enum('Invoice', 'Payment', 'Credit', 'Refund');
create table tbl_transactions
(
  transaction_id            int not null,
  type                      transaction_type,
  invoice_number            int not null, -- foreign key to invoice
  product_id                int, 
  units                     decimal(9,2) not null, -- 40 could be 40 hours of a service
  amount                    decimal(9,2) not null, -- 70 could be hourly rate
  total_amount              decimal(9,2) not null, -- calculated total
  date_created              date not null,
  user_created              int not null,
  date_modified             date not null,
  user_modified             int not null,
  primary key (transaction_id)
  -- service                     boolean,
  -- service_id                  int,
);

drop table if exists product;
create table tbl_products
(
  product_id                int not null,
  parent_product_id         int,
  description               varchar(200) not null,
  amount                    decimal(9,2) not null,
  tax_exempt                boolean,
  date_created              date not null,
  user_created              int not null,
  date_modified             date not null,
  user_modified             int not null,
  primary key (product_id)
);

-- unique constraints
-- foreign keys
-- indexes
-- sample data
-- views
-- triggers?
-- stored procs