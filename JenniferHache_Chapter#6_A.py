# Import Regular Expressions module
import re

def test_phone_number():
    # Create pattern to test phone number
    # only 123-123-1234 or 1231231234 format permitted
    pattern = r'^(?:\(\d{3}\)\s?|\d{3}[-]?)?\d{3}[-]?\d{4}$'

    while True:
        # ask user to enter phone number
        x = input('Enter Phone Number: ')
        # check if numbers entered matches pattern
        if re.match(pattern, x):
            print('Number accepted.')
            # return True for valid phone number
            return True
        else:
            # if number is invalid to pattern, ask user to try again
            print('Incorrect format. Please enter valid number again.')


def test_ssn():
    # Create pattern to test social security number
    # only 123-12-1234 or 123121234 format permitted
    pattern = r'^(?:\d{3}-\d{2}-\d{4}|\d{9})$'

    while True:
        # ask user to enter social security number
        x = input('Enter Social Security Number: ')
        # check if numbers entered matches pattern
        if re.match(pattern, x):
            print('Number accepted.')
            # return True for valid Social Security Number
            return True
        else:
            # if number is invalid to pattern, ask user to try again
            print('Incorrect format. Please enter valid number again.')


def test_zip_code():
    # Create pattern to test zip code
    # only 12345 or 12345-6789 format permitted
    pattern = r'^\d{5}(-\d{4})?$'

    while True:
        # ask user to enter zip code number
        x = input('Enter ZIP code: ')
        # check if numbers entered matches pattern
        if re.match(pattern, x):
            print('Number accepted.')
            # return True for valid zip code
            return True
        # if number is invalid to pattern, ask user to try again
        else:
            print('Incorrect format. Please enter valid number again.')

# Call validation functions
def main():
    print("\nvalidate the following inputs:")
    phone_valid = test_phone_number()
    ssn_valid = test_ssn()
    zip_valid = test_zip_code()

    print("\nOverall Validation:")
    print(f"Phone Number Valid: {phone_valid}")
    print(f"SSN Valid: {ssn_valid}")
    print(f"ZIP Code Valid: {zip_valid}")


# Call the main function to test program
if __name__ == "__main__":
    main()
