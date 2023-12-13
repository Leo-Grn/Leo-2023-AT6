class DataValidator:
    # Method to validate a list of strings
    def validate(self, input_list):
        result = []  # Initialize an empty list for valid numbers
        for item in input_list:
            if item.isdigit():  # Check if the item is a digit
                result.append(int(item))  # Add the integer to the result list
        return result  # Return the list of integers
