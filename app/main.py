import utils
import Ejercsv
import charts

def run():
    data = Ejercsv.read_csv('datos.csv')
    data = list(filter(lambda item: item['Continent'] == 'Europe', data))
    
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    
    
    country = input('Type country: ')
    charts.generate_bar_chart(country, countries, percentages)
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        
        # Verificar que los valores sean numéricos
        charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
    run()