Back-end NoSQL MongoDB

NoSQL, which stands for "Not Only SQL," refers to a category of database systems that do not strictly adhere to the traditional relational database management system (RDBMS) model based on tables and SQL for querying data. Instead, NoSQL databases are designed to handle large volumes of unstructured or semi-structured data and provide flexible schemas that can adapt to evolving data models.

Difference between SQL and NoSQL:

Data Model: SQL databases use a structured schema and tables with rows and columns, while NoSQL databases employ various data models, including document, key-value, wide-column, and graph.
Scalability: SQL databases typically scale vertically by adding more powerful hardware, whereas NoSQL databases are often designed for horizontal scalability across multiple servers or nodes.
Schema Flexibility: SQL databases enforce a rigid schema where table structures must be defined upfront, while NoSQL databases offer schema flexibility, allowing for dynamic and agile data modeling.
Complex Transactions: SQL databases support ACID transactions (Atomicity, Consistency, Isolation, Durability), while NoSQL databases prioritize availability and partition tolerance over strict consistency.
Query Language: SQL databases use Structured Query Language (SQL) for querying data, whereas NoSQL databases use various query languages or APIs tailored to their respective data models.
ACID:
ACID is an acronym that stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that guarantee the reliability of transactions in a database system:

Atomicity: Ensures that a transaction is treated as a single unit of work, meaning that either all of its operations are successfully completed, or none are applied at all.
Consistency: Guarantees that the database remains in a consistent state before and after the execution of a transaction, adhering to all defined rules and constraints.
Isolation: Ensures that the concurrent execution of transactions does not result in interference or data corruption, providing each transaction with the illusion of executing independently.
Durability: Ensures that once a transaction is committed, its changes are permanently stored in the database, even in the event of system failures or crashes.
Document Storage:
Document storage is a type of data storage model used in NoSQL databases where data is stored in the form of documents. Each document is a self-contained unit of data that can contain various types of information, such as key-value pairs, arrays, or nested documents. Document databases, such as MongoDB, Couchbase, and CouchDB, use this model to store and retrieve data efficiently, offering flexibility and scalability for handling diverse data structures.

NoSQL Types:
NoSQL databases can be categorized into four main types based on their data models:

Document-based: Stores data in flexible, semi-structured documents, often in JSON or BSON format. Examples include MongoDB, Couchbase, and CouchDB.
Key-value stores: Utilizes a simple key-value data model, where each item in the database is identified by a unique key. Examples include Redis, DynamoDB, and Riak.
Wide-column stores: Organizes data in tables with rows and columns, but with dynamic column families that can vary from row to row. Examples include Apache Cassandra and HBase.
Graph databases: Represents data as nodes, edges, and properties, allowing for the efficient traversal of complex relationships. Examples include Neo4j, Amazon Neptune, and JanusGraph.
Benefits of a NoSQL database:

Scalability: NoSQL databases offer horizontal scalability, enabling them to handle large volumes of data and high throughput.
Flexibility: NoSQL databases support flexible schemas, allowing for agile data modeling and accommodating evolving data structures.
Performance: NoSQL databases are optimized for specific use cases and can provide superior performance for certain types of workloads, such as real-time analytics and high-speed data ingestion.
High Availability: NoSQL databases are designed for distributed environments, providing built-in fault tolerance and high availability to ensure uninterrupted access to data.
Cost-effectiveness: NoSQL databases can be more cost-effective than traditional SQL databases for certain applications, particularly when dealing with massive datasets or cloud-based deployments.
Querying information from a NoSQL database:
Querying data from a NoSQL database depends on the specific type of NoSQL database being used and its corresponding query language or API. For example:

In a document-based NoSQL database like MongoDB, you can use the MongoDB Query Language (MQL) or methods provided by MongoDB drivers to query documents based on criteria like field values, array elements, and nested documents.
In a key-value store like Redis, you can use Redis commands such as GET, SET, HGET, and HSET to retrieve and manipulate key-value pairs.
In a wide-column store like Apache Cassandra, you can use CQL (Cassandra Query Language) to query data using SQL-like syntax, specifying columns, conditions, and sorting criteria.
Inserting/Updating/Deleting information from a NoSQL database:
Similarly, inserting, updating, and deleting data in a NoSQL database depends on the database type and its corresponding APIs or commands. For example:

In MongoDB, you can use methods like insertOne, updateOne, updateMany, deleteOne, and deleteMany to perform CRUD (Create, Read, Update, Delete) operations on documents.
In Redis, you can use commands like SET, HSET, DEL, and EXPIRE to insert, update, and delete key-value pairs or hash fields.
In Apache Cassandra, you can use CQL statements like INSERT, UPDATE, and DELETE to add, modify, or remove rows from tables.
How to use MongoDB:
To use MongoDB, you typically follow these steps:

Installation: Install MongoDB on your system or set up a cloud-based MongoDB service.
Initialization: Start the MongoDB server and configure it as needed, including setting up authentication, storage options, and replica sets for high availability.
Database Creation: Create a new database using the use command or by specifying a database name in your MongoDB client.
Collection Creation: Create collections within the database to store





