def base_url(is_live):
    if is_live:
        return "https://api.myidentitypass.com"
    else:
        return "https://sandbox.myidentitypass.com"
