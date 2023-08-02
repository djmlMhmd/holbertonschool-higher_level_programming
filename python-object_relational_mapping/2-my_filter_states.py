#!/usr/bin/python3

"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":

    """Connect to Mysql server"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    """Create a cursor object to execute queries"""
    cursor = db.cursor()

    """Execute the query to display same values with using format()"""
    cursor.execute(
        """
        SELECT *
        FROM states
        WHERE states.name LIKE BINARY '{}'
        ORDER BY states.id
        """.format(sys.argv[4])
    )

    """Fetch all the rows"""
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    """Close the cursor and database connection"""
    cursor.close()
    db.close()
