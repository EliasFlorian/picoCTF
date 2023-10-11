def decrypt_rsa(c, n, e):
    # Factor n using trial division
    def factorize(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                return i, n
        return n, 1

    p, q = factorize(n)

    # Calculate totient
    phi = (p - 1) * (q - 1)

    # Calculate modular inverse of e
    def modinv(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    d = modinv(e, phi)

    # Decrypt ciphertext
    m = pow(c, d, n)

    return m

# Provided values
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537

plaintext = decrypt_rsa(c, n, e)
print(plaintext)

