class Contact():
    def __init__(self, name='', phone='', email='', website='', birthday='', linkedin='', picture=''):
        self.name=name
        self.phone=phone
        self.email=email
        self.website=website
        self.birthday=birthday
        self.linkedin=linkedin
        self.picture=picture
        self.all_contact=[]
        self.single_contact={}

    def set_contact(self, name, phone, email, website, birthday, linkedin, picture):
        self.name=name
        self.phone=phone
        self.email=email
        self.website=website
        self.birthday=birthday
        self.linkedin=linkedin
        self.picture=picture

    def get_contact(self):
        return self.all_contact

    def create_contact(self):
        needs = ["name", "phone", "email", "website", "birthday", "linkedin", "picture"]
        for i in needs:
            self.single_contact[i]=raw_input("Enter your {}".format(i))
        self.set_add_contact(self.single_contact)


    def set_add_contact(self, contact={}):
        self.all_contact.append(contact)
        # print (self.all_contact)


    def get_delete_contact(self, name):
        all_contact=self.get_contact()
        if len(all_contact) > 0:
            for key,value in enumerate(all_contact):
                if name == value["name"]:
                    all_contact.pop(key)
                else:
                    print("No Contact to delete")
        else:
            print("No more contact to delete")

    def get_search_contact(self, name):
        all_contact = self.get_contact()
        if len(all_contact) > 0:
            for key, value in enumerate(all_contact):
                if name == value["name"]:
                    print(value)
        else:
            print("No contact to found")


# new_name=raw_input("What is your name?")
# new_phone=raw_input("Phone Number?")
# new_email=raw_input("What is your email?")
# new_website=raw_input("The name of your website?")
# dob=raw_input("Your date of birth?")
# linkedin=raw_input("LinkedIn Name?")
# pictureid=raw_input("Picture Id")

new_contact=Contact()

new_contact.create_contact()
user=raw_input("Enter the name you are searching for?")
new_contact.get_search_contact(user)
# value = " "
# while value != "Q":
#     print(new_contact.get_contact())
#     value=raw_input("Enter a name to delete")
#     new_contact.get_delete_contact(value)



# new_contact.set_contact(new_name, new_phone, new_email, new_website, dob, linkedin, pictureid)

# new_contact.get_contact()
