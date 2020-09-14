
def dragon_name(name, month):
    months = {
        'January': 'Scaly',
        'February':'Hot',
        'March':'Ice',
        'April':'SupaHotFire',
        'May':'ISpitThat',
        'June':'Arithmetic',
        'July':'Golden',
        'August':'san',
        'September':'chan',
        'October':'nim',
        'November':'popcorn',
        'December':'chocolate'
    }

    if month in months:
        return name + months[month]
    else:
        return "Please enter a valid month"


def penguin(name, month):
    month_switch={
        'January': 'Squawky',
        'February':'Fishy',
        'March':'Slick',
        'April':'Penguin #324',
        'May':'Flappy',
        'June':'Wheezy',
        'July':'Peggi',
        'August':'Slippin\'',
        'September':'Caruso',
        'October':'Mumble',
        'November':'Private',
        'December':'Kowalski'
    }
    
    new_name= f'{name} {month_switch[month]}'
    return new_name
    