from common import eprint

CORRECT_PASS = "pass"
print("cde job list --vcluster-endpoint https://d94tftqj.cde-64m2285t.dex-priv.xcu2-8y8x.dev.cldr.work/dex/api/v1")

# Simulate no line break at end of the line
print("WARN: Plaintext or insecure TLS connection requested, take care before continuing. Continue? yes/no [no]", end='')

i = input()
if i != "yes":
    eprint("Should've entered 'yes'. Exiting")
    exit(1)

print("API User Password: ")
password = input()
if password != CORRECT_PASS:
    eprint("Password is incorrect. Exiting")
    exit(2)

# Read json file and print it to stdout
json_file = "../resources/job-list-250dag.json"
with open(json_file) as f:
    print(f.read())