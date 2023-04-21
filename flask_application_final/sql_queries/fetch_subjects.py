# this fxn is useful when we want to get all the subjects of
#  a given year and department

# this fxn returns 1 and the list of tuples (each tuple
# containing subject details) for the correct input and returns
# 0 and the error in case of failed retreival of data
# (0,error) is passed in tuple form

from sql_queries import connection_fxn 


def select_required_subjects(correspondingYear, dept_name):
    connection = 0

    try:
        cursor=connection_fxn.make_connection()

        if (correspondingYear == "FY"):
            postgreSQL_select_Query = "select subject_name from sy_mp.subject where corresponding_year = '" + correspondingYear + "'"

        else:
            postgreSQL_select_Query = "select subject_name from sy_mp.subject where corresponding_year ='" + correspondingYear + "' and fk_dept_name = '" + dept_name + "'"

        cursor.execute(postgreSQL_select_Query)
        subject_details = cursor.fetchall()
        print("Yo")
        return 1, subject_details


    except (Exception, psycopg2.Error) as error:
        return 0, "Error while fetching data from PostgreSQL " + str(error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
