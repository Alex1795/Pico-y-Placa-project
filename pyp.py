import re
from datetime import date

class Consulta:

    #The __init__ function of the class takes the inputs assuming they were already checked by the Check function
    #Then it assigns the plate number. After that, it differentiates if the user gave a day name or a date as an input and
    #assigns it to the date_ member as the day name either directly or based on the 'days' list.
    #Finally it assigns the hour member of the class

    def __init__(self,number,date_,hour):

        days = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes','sabado','domingo')
        self.num   = number
        if date_ in days:
    # If the given date is the name of a day it assigns it to the date member in the class
            self.date  = date_
    # If it is a date it uses the datetime module and the list 'days' to assign the correct day to the variable
        else:
            day,month,year = date_.split('/')
            d = date(int(year), int(month), int(day))
            self.date = days[date.weekday(d)]

        self.hour = hour

    #This function first calls the predictor function.
    #Then it prints a prompt finalizing the program.
    def __str__(self):

        print(self.predictor())
        return 'Comprobacion finalizada'


    def predictor(self):
        #This function first takes the last digit of the plate, and checks if the given date is a Saturday or Sunday
        #where the restriction is not applied and returns an appropriate message.
        #It also contains a dictionary 'dias' containing the correspondent restricted numbers with the day name as the keys.
        #Then it creates a list with the applicable numbers for the given plate taken from the dictionary.
        #It also separates the given hour in hours and minutes and sums both to have a float number
        #After that the program checks if the given plate has a restriction on the given day, if it does not,
        #it returns an appropriate message.
        #If this statement is not true, then the function checks if the hour provided is inside the allowed hours. If it is
        #inside this time, it returns an appropriate message. If this statement is also false. It returns a message telling
        #the user the car cannot be on the road today.


        lastd = list(self.num)[-1]
        if self.date == 'sabado' or self.date == 'domingo':return('Hoy no se aplica restricción')

        dias = {'lunes':[1,2],'martes':[3,4],'miercoles':[5,6],'jueves':[7,8],'viernes':[9,0]}

        lst = dias[self.date]

        hora, minuto = str(self.hour).split(':')

        hour = float(hora) + float(minuto)/60


        if int(lastd) not in lst: return('Puede circular todo el día de hoy')

        elif (hour > 9.5 and hour < 16) or hour < 7 or hour > 19.5:
            return('Puede circular el día de hoy en este horario')

        else:return('No puede circular hoy en este horario. Puede circular hoy antes de las 7:00, después de las 19:30  y entre las 9:30 y 16:30')


def check(number = 0,date = 0,hour = 0):

    #This function has a list with the days of the week and three regex to check the user inputs.
    #It makes one check at a time, so a message can be shown to the user as soon as a wrong input is
    #received.
    #For the date it can accept either the day name or a date

    dias = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')

    #Checks if the input is in the form AAA-0000
    plate_re = re.compile(r'[A-Z][A-Z][A-z]-\d\d\d\d')
    #Checks if the input is in the form hours:minutes
    hour_re = re.compile(r'\d\d?:\d\d')
    #Checks if the input is in the form day/month/year
    date_re = re.compile(r'\d\d?/\d\d?/\d\d\d\d')

    if number != 0:
        if len(plate_re.findall(number)) == 0:raise SyntaxError('Por favor ingrese una placa valida en la forma: AAA-0000')
        return 0
    elif hour != 0:

        if len(hour_re.findall(hour)) == 0:raise SyntaxError('Por favor ingrese una hora separada por ":" ')

        hora, minuto = str(hour).split(':')

        if float(minuto) > 59:raise SyntaxError('La hora no puede tener mas de 59 minutos')

        return 0


    elif date != 0:
        if (date not in dias) and (len(date_re.findall(date)) == 0):raise SyntaxError('Por favor ingrese un día válido')

        return 0

    else: return 0

if __name__ == "__main__":
    # The prompts give the user the correct format to be input and checks it on every step

    num = input('Por favor ingrese su placa en la forma: AAA-0000\n')
    check  (num,0,0)

    # I implemented both ways to input a date, so the user can input 'lunes' or '06/03/2017' and get the same result.
    # The date format is the one used in Ecuador
    day = input('Por favor ingrese el día de la consulta en minúsculas o la fecha en formato dia/mes/año\n')
    check (0,day,0)

    hour = input('Por favor ingrese la hora de la consulta en formato 24hrs y separada por ":"\n')
    check (0,0,hour)

    pl = Consulta(num,day,hour) #Creates a Consulta object
    print(pl)                   #and prints it, where the predictor function is executed
    pass
