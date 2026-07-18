class Staff:
    def __init__(self, s_name, access_code):
        self.s_name = s_name
        self.__access_code = access_code

    # Property (Getter)
    @property
    def access_code(self):
        return self.__access_code

    # Property (Setter)
    @access_code.setter
    def access_code(self, new_code):
        if len(new_code) >= 6:
            self.__access_code = new_code
            print("Access code updated successfully.")
        else:
            print("Error: Access code must be at least 6 characters long.")

    # Display staff information
    def display_info(self):
        print("Staff Name:", self.s_name)
        print("Access Code:", self.__access_code)


# =====================
# Testing the program
# =====================

staff1 = Staff("ELISAH TWUMASI", "UMAT123")

# Display information
staff1.display_info()

# View access code
print("\nCurrent Access Code:", staff1.access_code)

# Update access code (Valid)
staff1.access_code = "Admin456"

# Display updated information
staff1.display_info()

# Update access code (Invalid)
staff1.access_code = "123"