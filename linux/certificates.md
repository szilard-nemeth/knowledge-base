# Certificates

## How to pass arguments like “Country Name” to OpenSSL when creating self signed certificate?
https://www.shellhacks.com/create-csr-openssl-without-prompt-non-interactive/

Example: 
```
openssl ... -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department/CN=example.com"
```