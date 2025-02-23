def get_user_data(conn, user_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()

def store_user_data(conn, user_data):
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name, email, risk_profile) VALUES (%s, %s, %s)",
            (user_data['name'], user_data['email'], user_data['risk_profile'])
        )
        conn.commit()

def update_user_data(conn, user_id, updated_data):
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE users SET name = %s, email = %s, risk_profile = %s WHERE id = %s",
            (updated_data['name'], updated_data['email'], updated_data['risk_profile'], user_id)
        )
        conn.commit()

def delete_user_data(conn, user_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()