def encode_gender(gender):
    """
    This function will accept the gender and encode it in binary
    Input: gender : str
    Output: res : int
    """
    if gender.lower() == 'male':
        return 0
    if gender.lower() == 'female':
        return 1

def encode_smoker(smoker):
    """
    This function will accept the gender and encode it in binary
    Input: gender : str
    Output: res : int
    """
    if smoker.lower() == 'no':
        return 0
    if smoker.lower() == 'yes':
        return 1