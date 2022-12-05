import argparse
import json
import sys


def main(argv):
    # Create the parser
    my_parser = argparse.ArgumentParser(description='This program has to filter a list of elements containing a pattern and counts of People and Animals by counting the number of children ')

    # Add the arguments
    my_parser.add_argument('--filter',
                        metavar='Filter',
                        type=str,
                        help='filter a list of elements containing a pattern')
    my_parser.add_argument('--count',
                        action='store_true',
                        help='the counts of People and Animals by counting the number of children')


    # Execute the parse_args() method
    args = my_parser.parse_args(argv)
    Filter= args.filter
    count = args.count

    data_filtered =[]
    list_count = []
    
    #Path to the data.json
    path = "C:\\Users\\tahar\\Desktop\\Backend\\backend\\backend-test\\backend-test\\data.json"

    # Python program to read
    # json file and convert them to list python 
    with open(path) as f:
        data = json.load(f)
        # Filter 
        if Filter:
            data_filtered=[dico for dico in data for dict1 in dico['people'] for animal in dict1['animals'] if Filter in animal['name']]
            if len(data_filtered) != 0:
                return data_filtered
            else:
                print('There is no aniamls which containing ',Filter,' in theire names')
        # Count
        elif count:
            for dico in data:
                children = 0
                for ele in dico['people']:
                    animals = len(ele['animals'])
                    children += 1 + animals
                    ele['name'] += f" [{animals}]"
                dico['name'] += f" [{children}]"
                list_count.append(dico)
            return list_count

        else:
            print('There is no argument suplied, please make -h to see all options')

if __name__ == '__main__':
    print(main(sys.argv[1:]))

