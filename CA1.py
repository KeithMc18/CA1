class Patient:
    __firstName = ''
    __surname = ''
    __hasMedCard = False
    __isPrivatePatient = False
    __daysInHospital = 1

    def __init__(self, f_name='', l_name='', med_card_holder=False, is_private=False, days_stayed=1):
        self.__firstName = f_name
        self.__surname = l_name
        self.__hasMedCard = med_card_holder
        self.__isPrivatePatient = is_private
        self.__daysInHospital = days_stayed

    def add_night_stay(self, days_stayed):
        if days_stayed <= 1:
            self.__daysInHospital = 1
        else:
            self.__daysInHospital = days_stayed
        return self.__daysInHospital

    def getFirstName(self):
        return self.__firstName

    def getsurName(self):
        return self.__surname

    new_bill_cost = 0

    def calculate_bill(self):
        total_bill_cost = 0.0
        if self.__hasMedCard is True:
            new_bill_cost = total_bill_cost
        elif self.__hasMedCard is False and self.__isPrivatePatient is False:
            new_bill_cost = self.add_night_stay(self.__daysInHospital) * 100
        else:
            new_bill_cost = self.add_night_stay(self.__daysInHospital) * 20
        return new_bill_cost

    def print_patient_details(self):
        print('Patients Name :                          ', self.getFirstName(), self.getsurName())
        print('Patients Medical Card holder :           ', self.__hasMedCard)
        print('Patients has Private Care                ', self.__isPrivatePatient)
        print('Patients Duration Stayed :               ', self.add_night_stay(self.__daysInHospital))
        print('Patients Bill € :                        ', self.calculate_bill())


# This is the test for part h) as well as 2 extra tests for myself


p1 = Patient('Jane', 'Doe', True, True, 3)
p1.print_patient_details()
print('*----------------------------------------------*')
p2 = Patient('Joe', 'Bloggs', False, True, 5)
p2.print_patient_details()
print('*-----------------------------------------------*')
p3 = Patient('John', 'Smith', False, True, 10)
p3.print_patient_details()
print('*-----------------------------------------------*')
p4 = Patient('Ran', 'Domer', False, False, 4)
p4.print_patient_details()
print('*-----------------------------------------------*')
p5 = Patient('Som', 'Eone', True, False, 20)
p5.print_patient_details()


patient_list = []

menu = int(input('Would you like to enter a new patient to the system(1) or exit the system(2)'))

if menu == 1:
    f_name_in = str(input('Please enter the patients first name '))
    if f_name_in == ' ':
        print('You must enter a real name!')
    l_name_in = str(input('Please enter the patients surname '))
    if f_name_in == ' ':
        print('You must enter a real name!')
    med_card_in = str(input('Does the Patient have a medical card?(Y/N)'))
    if med_card_in.upper() == 'Y':
        med_card_in = True
    else:
        med_card_in = False
    is_private_in = str(input('Does the Patient have private health insurance?(Y/N) '))
    if is_private_in.upper() == 'Y':
        is_private_in = True
    else:
        is_private_in = False
    days_stayed = int(input('Please enter the number of days stayed by the patient '))

    new_pat = Patient(f_name_in, l_name_in, med_card_in, is_private_in, days_stayed)
    patient_list.append(new_pat)
    menu = int(input('Would you like to enter a new patient to the system(1) or exit the system(2)'))

else:
    print('Thanks for adding to the patient list!')
    print(patient_list)


