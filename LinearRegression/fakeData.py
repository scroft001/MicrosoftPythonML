from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Function to generate random log data
def generate_log_entry():
	name = fake.name()
	address = fake.address()
	real_address = address.replace('\n', ' ')
	login_time = fake.date_time_this_decade()
	ping = random.randint(20, 100)
	ip_address = fake.ipv4()
	page_url = random.choice(["/login.php", "/index.html", "/customers.html", "/contact.hmtl", "/features.html", "/posts.php"])
	time_on_server = random.randint(10, 120)
	encryption_type = random.choice(["AES-128", "AES-192", "AES-256", "RSA-2048", "RSA-3072", "RSA-4096"])

	return [name, real_address, login_time, ping, ip_address, page_url, time_on_server, encryption_type]

# Create a table with 500 entries
table_data = []
for _ in range(500):
	entry = generate_log_entry()
	table_data.append(entry)

print(table_data)












