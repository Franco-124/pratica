#Leer y manipular csv

import csv


def read_csv(path):
    try:
        with open(path, mode ='r')as file:
            reader = csv.reader(file, delimiter=",")
            header=next(reader)
            print(header)
            data=[]
            for row in reader:
                iterable=zip(header, row)
                country_dict ={key : value for key,value in iterable}
                data.append(country_dict)
            return data
    except FileNotFoundError:
        print('File not found')
        


if __name__ == '__main__':
    data=read_csv('app/datos.csv')

    print(data[0])