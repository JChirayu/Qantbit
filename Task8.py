statement = 'Contact us at support@example.com or admin@example.org.'
emails = []
a = statement.split(' ')

for item in a:
    if '@' and '.' in item:
        emails.append(item)

print(emails)