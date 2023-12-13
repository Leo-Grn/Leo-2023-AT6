class DataValidator:
    # Method to validate a list of strings for positive integers
    def validate(self, input_list):
        result = []  # Initialize an empty list for valid numbers
        for item in input_list:
            if item.isdigit() and int(item) > 0:  # Check if the item is a positive digit
                result.append(int(item))  # Add the positive integer to the result list
        return result  # Return the list of positive integers
