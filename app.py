import json
import argparse
from argparse import Namespace
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


def configure_arg_parser() -> Namespace:
    parser = argparse.ArgumentParser(description='KBO Linked Data Event Stream tool')
    subparsers = parser.add_subparsers(dest='command')
    # loadfull command
    parser_loadfull = subparsers.add_parser('loadfull', help='Loads KBO data into a local SQLite DB under the data folder.')
    parser_loadfull.add_argument('date', help='The date of the dump to use.')
    # loaddiff command
    parser_load_diff = subparsers.add_parser('loaddiff', help='Loads KBO data into a local SQLite DB under the data folder.')
    parser_load_diff.add_argument('date', help='The date of the diff dump to use.')
    # dump_ldes command
    parser_dump_ldes = subparsers.add_parser('dump_ldes', help='Dumps thefull KBO LDES collection.')
    parser_dump_ldes.add_argument('--format', help='The format to dump the data in.', choices=['json', 'json-ld', 'turtle'], default='turtle')
    parser_dump_ldes.add_argument('--blank-nodes', default='no', type=str, help='use blank nodes in rdf.', choices=["yes", "no"])
    # sample command
    parser_sample = subparsers.add_parser('sample', help='Stop synchronizing a previously onboarded LDES collection with given alias.')
    parser_sample.add_argument('enterprise_nr', help='The enterprise number to use as a sample.')
    parser_sample.add_argument('--format', help='The format to dump the data in.', choices=['json', 'json-ld', 'turtle'], default='turtle')
    parser_sample.add_argument('--blank-nodes', default='no', type=str, help='use blank nodes in rdf.', choices=["yes", "no"])
    return parser

if __name__ == '__main__':
    parser = configure_arg_parser()
    args = parser.parse_args()

    if args.command == 'loadfull':
        diff_name = args.date
        loader= DataLoader(BASE_PATH, diff_name, DB_LOCATION)
        loader.load_data()
        exit()
    elif args.command == 'loaddiff':
        print("Loding difference files is not supported yet.") 
        exit()
    elif args.command == 'dump_ldes':
        format = args.format
        blank_nodes = args.blank_nodes == "yes"
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
        enterprise_nr = args.enterprise_nr
        format = args.format
        blank_nodes = args.blank_nodes == "yes"
        enterprise = KboGenerator(BASE_PATH, DB_LOCATION).one(enterprise_nr)
        if format == "json":
            print(json.dumps(enterprise.to_dict(), indent=4))
            exit()
        else:
            graph = Graph()
            graph.bind("kbo", KBO)
            graph.bind("org", ORG)
            graph.bind("foaf", FOAF)
            graph.bind("vcard", VCARD)
            graph.bind("locn",LOCN)
            graph.bind("legal",LEGAL)
            graph.bind("terms",TERMNAME)
            enterprise.to_rdf(graph, with_blank_nodes=blank_nodes)
            print(graph.serialize(format=format))
            exit()

