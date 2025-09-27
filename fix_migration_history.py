import sqlite3

DB_PATH = 'db.sqlite3'

def remove_migration(app, name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM django_migrations WHERE app = ? AND name = ?", (app, name))
    conn.commit()
    conn.close()
    print(f"Removed migration {app}.{name} from django_migrations table.")

def remove_all_migrations_for_apps(apps):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    placeholders = ','.join('?' for _ in apps)
    cursor.execute(f"DELETE FROM django_migrations WHERE app IN ({placeholders})", apps)
    conn.commit()
    conn.close()
    print(f"Removed all migrations for apps {apps} from django_migrations table.")

def main():
    print("Removing all admin, jobs, and accounts migration records...")
    remove_all_migrations_for_apps(['admin', 'jobs', 'accounts'])

    print("Now you can run:")
    print("  python manage.py migrate accounts")
    print("  python manage.py migrate jobs")
    print("  python manage.py migrate admin")

if __name__ == '__main__':
    main()
