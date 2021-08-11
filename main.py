from lib.math import invmod
from lib.generators import n_num_gen, e_num_gen

n, fi_n = n_num_gen(int(input('Enter the maximum number to find a prime number: ')))
e = e_num_gen(fi_n)
d = invmod(e, fi_n)

# public key
pk = [e, n]
# secret key
sk = [d, n]

msg = int(input(f'Choose a message between 1 and {n}: '))

cypher_msg = (msg ** e) % n
decrypted_msg = (cypher_msg ** d) % n

print(f"""
Number N: {n}
Number E: {e}
Number D: {d}
Public key: {pk}
Secret key: {sk}
Message: {msg}
Encrypted message: {cypher_msg}
Decrypted message: {decrypted_msg}
""")