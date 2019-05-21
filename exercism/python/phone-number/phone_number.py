import re

class Phone(object):
    def __init__(self, phone_number):
        number_dirty = ''.join(re.findall(r'\d+', phone_number))
        
        # verify correct number of digits
        if (len(number_dirty) < 10) or (len(number_dirty) > 11):
            raise ValueError("incorrect number of digits")
            return
        
        # verify correct country code, if included, and remove
        if (len(number_dirty)) == 11:
            if number_dirty[0] != '1':
                raise ValueError("incorrect country code")
                return
            else:
                number_dirty = number_dirty[1:11]
        
        # verify first digit valid for area code and exchange code
        if (int(number_dirty[:1]) < 2) or (int(number_dirty[3:4]) < 2):
            raise ValueError("invalid area code or exchange code")
            return

        # number is now clean
        self.number = number_dirty
        self.area_code = number_dirty[0:3]

    def pretty(self):
        return f'({self.number[0:3]}) {self.number[3:6]}-{self.number[6:10]}'
