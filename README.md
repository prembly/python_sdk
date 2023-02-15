# Library Usage

Install the package using python installer and also register on prembly to get your API key.
```text
pip install prembly or pip3 install prembly
```

## USES

```python
from prembly.prembly import DataVerification

v = DataVerification(apikey="Your API KEY", is_live=False, country="Country data to be Access")

data = v.get_bank_code() ## Call the method of data you want to access
```
NOTE: To use the test kindly set the *is_live* to False and when you're done and ready to go live, set *is_live* to True.
Also, if the country data you are trying access is not set, the default *NGN* will be set.

## List of Methods Available
NIGERIA
1. credit_bureau_with_bvn
2. vehicle_verification
3. bvn_or_phone
4. bvn_with_face_validation
5. bvn
6. nin_slip
7. nin
8. nin_with_face_validation
9. bvn_nin_phone
10. tax_identification
11. basic_company_search
12. advance_company_search
13. basic_phone_number
14. advance_phone_number
15. get_bank_code
16. basic_account_verification
17. advance_account_verification
18. voters_card_with_image
19. voters_card
20. basic_drivers_licence
21. advance_drivers_licence
22. drivers_licence
23. credit_bureau
24. international_passport

OTHER Country coming soon