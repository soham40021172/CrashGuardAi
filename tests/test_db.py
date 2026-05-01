from crash_report.db.connection import DatabaseConnection

db = DatabaseConnection()
engine = db.get_engine()

print("Connected Successfully!")