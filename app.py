import json
import argparse
from rdflib import Graph, ORG, FOAF, SKOS
from namespace.kbo import KBO
from namespace.vcard import VCARD
from namespace.locn import LOCN
from namespace.legal import LEGAL
from namespace.termname import TERMNAME
from pyldes_kbo.services.data_loader import DataLoader
from pyldes_kbo.services.kbo_generator import KboGenerator

"""
Free geocoding: https://geocode.maps.co/
example: https://geocode.maps.co/search?q=Ter+Voortlaan+26+2650+edegem+belgium
"""
#Uses relative path
VERSION = "KboOpenData_2022_11"
DB_LOCATION = "data/kbo.db"
BASE_PATH='data'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the KBO example.')
    parser.add_argument('command', type=str, choices=['load', 'run', 'sample','version_sample','version_run'], help='Command to run')
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
            graph.bind("locn", LOCN)
            graph.bind("legal", LEGAL)
            graph.bind("terms", TERMNAME)
            enterprise.to_rdf(graph, with_blank_nodes=False)
            print(graph.serialize(format='turtle'))
            #print(f"Processing record {current_rec} of {total_records} [{current_rec/total_records*100:.2f}%]\r", end="")
            print(f"Processing record {current_rec} of {total_records} [{current_rec/total_records*100:.2f}%]")

    elif args.command == 'sample':
        enterprise = KboGenerator(BASE_PATH, DB_LOCATION).one("0414.881.767")
        graph = Graph()

        #bind kbo, org, foaf, vard prefix.
        graph.bind("kbo", KBO)
        graph.bind("org", ORG)
        graph.bind("foaf", FOAF)
        graph.bind("vcard", VCARD)
        graph.bind("locn",LOCN)
        graph.bind("legal",LEGAL)
        graph.bind("terms",TERMNAME)

        enterprise.to_rdf(graph, with_blank_nodes=False)
        ent_dict = enterprise.to_dict()
        #print(json.dumps(ent_dict, indent=4))
        #print(ent_dict)
        print(graph.serialize(format='turtle'))
    # Get one versioned KBO Enterprise Entity
    elif args.command == 'version_sample':
        enterprise = KboGenerator(BASE_PATH, DB_LOCATION).one("0416.822.559")
        graph = Graph()

        # bind kbo, org, foaf, vard prefix.
        graph.bind("kbo", KBO)
        graph.bind("org", ORG)
        graph.bind("foaf", FOAF)
        graph.bind("vcard", VCARD)
        graph.bind("locn", LOCN)
        graph.bind("legal", LEGAL)
        graph.bind("terms", TERMNAME)

        enterprise.to_rdf_version(graph, with_blank_nodes=False)
        ent_dict = enterprise.to_dict()
        # print(json.dumps(ent_dict, indent=4))
        # print(ent_dict)
        print(graph.serialize(format='turtle'))

    # Get versioned KBO Enterprise Entities
    elif args.command == 'version_run':
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
            graph.bind("locn", LOCN)
            graph.bind("legal", LEGAL)
            graph.bind("terms", TERMNAME)
            enterprise.to_rdf_version(graph, with_blank_nodes=False)
            print(graph.serialize(format='turtle'))
            # print(f"Processing record {current_rec} of {total_records} [{current_rec/total_records*100:.2f}%]\r", end="")
            print(f"Processing record {current_rec} of {total_records} [{current_rec / total_records * 100:.2f}%]")