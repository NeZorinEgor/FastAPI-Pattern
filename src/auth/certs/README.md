Your RSA keys heer.

Generation of `RSA` keys for JWT: 
```bash
# Generate an RSA private key of size 2048
openssl genrsa -out jwt-private.pem 2048
# Extract a public key from a key pair that can be used in a certificate
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```