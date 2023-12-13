class DataValidator:
    # Method to validate a list of strings for positive integers
    def validate(self, input_strings):
        valid_numbers = []  # Initialize an empty list for valid numbers
        for string in input_strings:
            if string.isdigit() and int(string) > 0:  # Check if string is a positive integer
                valid_numbers.append(int(string))  # Add the integer to the valid numbers list
        return valid_numbers  # Return the list of valid positive integers
