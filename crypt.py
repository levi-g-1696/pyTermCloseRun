from cryptography.fernet import Fernet


key = Fernet.generate_key()
print(key)

key = b'PCHl_MjGyEyBxLYha3S-cWg_SDDmjT4YYaKYh4Z7Yug='
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"SQLShack@DemoPas3s")
print(ciphered_text)


key = b'PCHl_MjGyEyBxLYha3S-cWg_SDDmjT4YYaKYh4Z7Yug='
cipher_suite = Fernet(key)
#ciphered_text = b'gAAAAABd_jcLWEz-fIBt3y2P3IoB3jGdbNnSzeSINZ8BomP9DrKIX2YF4pMLkMCvCxLshmKgKXk7np42xop6QIaiawbhjGayMU0UrbTeUX-6XA8zmo55vwA='
unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)
