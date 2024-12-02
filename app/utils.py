def get_population(country_dict :dict):
    population_dict={
        '2022':int(country_dict['2022 Population']),    '2020':country_dict['2022 Population'],
        '2015':int(country_dict['2022 Population']),
        '2010':int(country_dict['2022 Population']),
        '2000':int(country_dict['2022 Population']),        '1990':country_dict['2022 Population'],
        '1980':int(country_dict['2022 Population']),
       '1970':int(country_dict['2022 Population']),  }
    labels= population_dict.keys()
    values = population_dict.values()
    
    return labels, values
 

def population_by_country(data, country):
    result=list(filter(lambda item : item['Country/Territory']==country,data ))
    return result

def get_population_percentaje(data):
    labels=[country['Country/Territory'] for country in data]
    values=[float(country['World Population Percentage']) for country in data]
    return labels, values