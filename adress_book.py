def input_person():
    print("\n" + "Please input known information if available. If not available then input an \"/\"" + "\n")
    
    first_name = input("First Name: ").capitalize()
    last_name = input("Last Name: ").capitalize()
    birthday = input("Birthday (Please input date in YYYY/MM/DD format): ")
    phone_number = (input("Phone Number (Please input Phone Number in this +49 162 3718384 format): "))
    email = input("Email: ").lower()
    
    print("\n" + "Information received")
    return Person(first_name, last_name, birthday, phone_number, email)
    
class Person:
    def __init__(self, first, last, birthday, phone_number, email):
        self.first = first
        self.last = last
        self.birthday = birthday
        self.phone_number = phone_number
        self.email = email
        
    def full_name(self):
        print(f'{self.first} {self.last}')
        
    def __str__(self):
        return_string = 20 * "-" + "\n"
        
        return_string += f"{self.first} {self.last} | Birthday: {self.birthday}\n"
        return_string += f"{self.phone_number} | {self.email}\n"
        
        return_string += 10 * "-" + "\n"
        
        return return_string
    
    def save_to_json(self, filename):
        person_dict = {'first_name': self.first, 'last_name': self.last, 'birthday': self.birthday, 'phone_number': self.phone_number, 'email': self.email}
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict, indent = 2))
            
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
            
        self.first = data['first_name']
        self.last = data['last_name']
        self.birthday = data['birthday']
        self.phone_number = data['phone_number']
        self.email = data['email']
    
def new_person():
    person = input_person()
    print(person)

if __name__ == "__main__":
    while True:
        perform_action = input("Would you like to create a new person(n) / list of all people (l) / edit a person (e) / exit program (Exit / x) ? \nChoice: ")
        perform_action.upper().lower()
        
        if  (perform_action == "n"):
            new_person()
            #TODO: save the new person
        elif (perform_action == "l"):
            #TODO: list all people 
            print(perform_action)
        elif (perform_action == "e"):
            #TODO: list all people
            #TODO: choice person
            #TODO: edit person
            print(perform_action)
        elif (perform_action == "exit" or "x"):
            exit()
        else:
            print("invalid action")