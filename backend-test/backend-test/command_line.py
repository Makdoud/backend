import argparse
import json


def main():
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
    args = my_parser.parse_args()
    Filter= args.filter
    count = args.count

    data_filtered =[]

    # Python program to read
    # json file and filter
    with open('/tmp/data.json') as f:
        data = json.load(f)
        if Filter:
            data_filtered=[dico for dico in data for dict1 in dico['people'] for animal in dict1['animals'] if Filter in animal['name']]
            if len(data_filtered) != 0:
                print(data_filtered)
            else:
                print('There is no aniamls which containing ',Filter,' in theire names')
        elif count:
            for dico in data:
                print('-',sum(1 for v in dico.values()))
        else:
            print('There is no argument suplied, please make -h to see all options')

if __name__ == '__main__':
    main()

