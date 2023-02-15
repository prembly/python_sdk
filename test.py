from prembly.prembly import DataVerification

v = DataVerification(apikey="aN6htsV9.StLQmruQ5iDzdu6FtDzyGMJUKpeHGs4e", is_live=True)

# d = v.credit_bureau(bvn_number="22164769809")
d = v.get_bank_code()
print(d)
