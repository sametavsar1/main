from sqlalchemy import create_engine, text

# PostgreSQL bağlantı bilgilerini tanımla
db_username = "admin"
db_password = "user1234"
db_host = "localhost"
db_port = "5434"
db_name = "PSQLDB"

# PostgreSQL bağlantı dizesini oluştur
db_url = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# SQLAlchemy engine oluştur
engine = create_engine(db_url)

# Oluşturulan engine üzerinden bağlantı kur
conn = engine.connect()

# Kullanıcıdan ad ve soyad bilgilerini al
userId = input("UserID girin: ")
passw = input("Pass girin: ")

# Sorguyu oluştur ve kullanıcıdan alınan bilgileri ekle
query = text("INSERT INTO identity (username, pass) VALUES (:first_name, :last_name);")
conn.execute(query, {'first_name': userId, 'last_name': passw})

# Bağlantıyı kapat
conn.close()

print('İşlem tamamlandi.')
