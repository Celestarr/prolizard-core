from django.db import connection


def get_username_sequence_value():
    with connection.cursor() as cursor:
        cursor.execute("SELECT nextval('core_users_username_seq')")
        return cursor.fetchone()[0]
