from requests import request as req
import json
from .base import base_url
import pathlib


class DataVerification:
    def __init__(self, apikey: str = None, is_live: bool = False, country: str = "NGN"):
        self.apikey = apikey
        self.is_live = is_live
        self.country = country
        self.verify = f"{pathlib.Path(__file__).parent.resolve()}/certs.pem"

    def headers(self):
        return {
            'Content-Type': 'application/json',
            'x-api-key': self.apikey
        }

    def credit_bureau_with_bvn(self, bvn_number: str):
        """
        This method is used to check credit score/record of user.
        :param bvn_number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/custom/bvn_w_credit"
            payload = json.dumps(dict(number=bvn_number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def vehicle_verification(self, vehicle_number: str):
        """
        This method is used to check vehicle registration
        :param vehicle_number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/vehicle"
            payload = json.dumps(dict(vehicle_number=vehicle_number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def bvn_or_phone(self, channel: str, number: str):
        """
        This method allow user to verify customer either by using BVN or Mobile number
        :param channel:
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/bp/verification"
            payload = json.dumps(dict(channel=channel, number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def bvn_with_face_validation(self, image: str, number: str):
        """
        This method take in BVN and Image URL(png, jpeg base64)
        :param image:
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/bvn_w_face"
            payload = json.dumps(dict(image=image, number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def bvn(self, number: str):
        """
        This method return detailed information about user using bank verification number(BVN)
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/bvn"
            payload = json.dumps(dict(number=number))
            response = req("POST", url, headers=self.headers(), data=payload)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def nin_slip(self, image: str):
        """
        This method take in the NIN slip of the customer and use it search for the owner of the NIN
        :param image:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/nin/image"
            payload = json.dumps(dict(image=image))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def nin(self, number: str):
        """
        This method allow user to lookup a national identification number
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/nin_wo_face"
            payload = json.dumps(dict(number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def nin_with_face_validation(self, image: str, number: str):
        """
        This method allow user to verify user NIN against user's Image
        :param image:
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/nin"
            payload = json.dumps(dict(image=image, number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def bvn_nin_phone(self, number: str):
        """
        This endpoint allows you to verify bank verification number,
        national identity number and phone number in just a single API request
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/bvn_nin_phone"
            payload = json.dumps(dict(number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def tax_identification(self, channel: str, number: str):
        """
        This method allows you to verify a tax identification number.
        channel takes in (TIN, CAC, Phone): TIN is default
        :param channel:
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/tin"
            payload = json.dumps(dict(channel=channel, number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def basic_company_search(self, rc_number: str, company_name: str):
        """
        This method allows you to verify an RC number of a business
        :param rc_number:
        :param company_name:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/cac"
            payload = json.dumps(dict(rc_number=rc_number, company_name=company_name))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def advance_company_search(self, rc_number: str, company_name: str):
        """
        This method allows you to verify an RC number of a business and get more or advance details about the company
        :param rc_number:
        :param company_name:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/cac"
            payload = json.dumps(dict(rc_number=rc_number, company_name=company_name))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def basic_phone_number(self, number):
        """
        This method allow you to lookup for a number
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/phone_number"
            payload = json.dumps(dict(number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def advance_phone_number(self, number):
        """
        This method allow you to lookup for a number and get more/comprehensive information
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/phone_number/advance"
            payload = json.dumps(dict(number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def get_bank_code(self):
        """
        This method is used to get all Nigeria bank code
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/bank_code"
            response = req("GET", url, headers=self.headers(), verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def basic_account_verification(self, bank_code: str, account_number):
        """
        Basic Account Verification
        :param bank_code:
        :param account_number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/bank_account"
            payload = json.dumps(dict(number=account_number, bank_code=bank_code))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def advance_account_verification(self, bank_code: str, account_number):
        """
        Advance Bank Verification
        :param bank_code:
        :param account_number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/bank_account/advance"
            payload = json.dumps(dict(number=account_number, bank_code=bank_code))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def voters_card_with_image(self, image: str):
        """
        Voter card with image
        :param image:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/voters_card/image"
            payload = json.dumps(dict(image=image))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def voters_card(self, state: str, last_name: str, number: str):
        """
        This method allows you to verify voter's card number
        :param state:
        :param last_name:
        :param number:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/voters_card"
            payload = json.dumps(dict(state=state, last_name=last_name, number=number))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def basic_drivers_licence(self, first_name: str, last_name: str, number: str, dob: str):
        """
        Date Format: 1998-06-19 - Format
        :param first_name:
        :param last_name:
        :param number:
        :param dob:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/drivers_licence/basic"
            payload = json.dumps(dict(first_name=first_name, last_name=last_name, number=number, dob=dob))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def advance_drivers_licence(self, first_name: str, last_name: str, number: str, dob: str):
        """
         Date Format: 1998-06-19 - Format
        :param first_name:
        :param last_name:
        :param number:
        :param dob:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/drivers_licence/advance"
            payload = json.dumps(dict(first_name=first_name, last_name=last_name, number=number, dob=dob))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def drivers_licence(self, number: str, dob: str):
        """
         Date Format: 1998-06-19 - Format
        :param number:
        :param dob:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/drivers_licence"
            payload = json.dumps(dict(number=number, dob=dob))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def credit_bureau(self, phone_number: str, first_name: str):
        """
        This method allows you to get credit bureau statement of a user
        :param phone_number:
        :param first_name:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/credit_bureau"
            payload = json.dumps(dict(phone_number=phone_number, first_name=first_name))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")

    def international_passport(self, first_name: str, last_name: str, number: str, dob: str):
        """
         Date Format: 1998-06-19 - Format
        :param first_name:
        :param last_name:
        :param number:
        :param dob:
        :return:
        """
        if self.country == "NGN":
            url = f"{base_url(self.is_live)}/api/v1/biometrics/merchant/data/verification/national_passport"
            payload = json.dumps(dict(first_name=first_name, last_name=last_name, number=number, dob=dob))
            response = req("POST", url, headers=self.headers(), data=payload, verify=self.verify)
            data = json.loads(response.text)
            return data
        else:
            return dict(staus=False, message="permission denied", reason="This function is only available in Nigeria")