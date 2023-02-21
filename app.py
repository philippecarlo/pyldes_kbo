import json
import argparse
from rdflib import Graph, ORG, FOAF, SKOS
from namespace.kbo import KBO
from namespace.vcard import VCARD
from pyldes_kbo.services.data_loader import DataLoader
from pyldes_kbo.services.kbo_generator import KboGenerator

"""
Free geocoding: https://geocode.maps.co/
example: https://geocode.maps.co/search?q=Ter+Voortlaan+26+2650+edegem+belgium
"""

VERSION = "KboOpenData_2022_11"
DB_LOCATION = "/mnt/c/dev/imec-ldes/pyldes_kbo/data/kbo.db" 
BASE_PATH='/mnt/c/dev/imec-ldes/pyldes_kbo/data' 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the KBO example.')
    parser.add_argument('command', type=str, choices=['load', 'run', 'sample'], help='Command to run')
    args = parser.parse_args()
    if args.command == 'load':
        loader= DataLoader(BASE_PATH, VERSION, DB_LOCATION)
        loader.load_data()
    elif args.command == 'run':
        enterprises = KboGenerator(BASE_PATH, DB_LOCATION)
        total_records = enterprises.count()
        current_rec = 0
        for enterprise in enterprises.generate():
            current_rec = current_rec + 1
            graph = Graph()
            graph.bind("kbo", KBO)
            graph.bind("org", ORG)
            graph.bind("foaf", FOAF)
            graph.bind("vcard", VCARD)
            enterprise.to_rdf(graph, with_blank_nodes=False)
            print(graph.serialize(format='turtle'))
            #print(f"Processing record {current_rec} of {total_records} [{current_rec/total_records*100:.2f}%]\r", end="")
            print(f"Processing record {current_rec} of {total_records} [{current_rec/total_records*100:.2f}%]")
    elif args.command == 'sample':
        enterprise = KboGenerator(BASE_PATH, DB_LOCATION).one("0416.822.559")
        graph = Graph()
        
        graph.bind("kbo", KBO)
        graph.bind("org", ORG)
        graph.bind("foaf", FOAF)
        graph.bind("vcard", VCARD)
        
        enterprise.to_rdf(graph, with_blank_nodes=False)
        ent_dict = enterprise.to_dict()
        #print(json.dumps(ent_dict, indent=4))
        print(graph.serialize(format='turtle'))

