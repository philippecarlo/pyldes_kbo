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
from namespace.geo import GEO

"""
Free geocoding: https://geocode.maps.co/
example: https://geocode.maps.co/search?q=Ter+Voortlaan+26+2650+edegem+belgium
"""
#Uses relative path
VERSION = "KboOpenData_2022_11"
DB_LOCATION = "data/kbolaunch.db"
BASE_PATH='data'
BEL_20=["0417.497.106",
        "0404.616.494",
        "0877.248.501",
        "0451.406.524",
        "0401.277.914",
        "0818.292.196",
        "0426.184.049",
        "0400.378.485",
        "0403.448.140",
        "0476.388.378",
        "0466.460.429",
        "0407.040.209",
        "0403.227.515",
        "0202.239.951",
        "0403.219.397",
        "0403.091.220",
        "0403.053.608",
        "0401.574.852",
        "0887.216.042",
        "0417.199.869"]

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

    # dump_ldes command (versioned)
    parser_dump_ldes = subparsers.add_parser('version_dump_ldes', help='Dumps the full versioned KBO LDES collection.')
    parser_dump_ldes.add_argument('--format', help='The format to dump the data in.',
                                  choices=['json', 'json-ld', 'turtle'], default='turtle')
    parser_dump_ldes.add_argument('--blank-nodes', default='no', type=str, help='use blank nodes in rdf.', choices=["yes", "no"])

    # sample command (versioned)
    parser_sample = subparsers.add_parser('version_sample',  help='Stop synchronizing a previously onboarded LDES collection with given alias.')
    parser_sample.add_argument('enterprise_nr', help='The enterprise number to use as a sample.')
    parser_sample.add_argument('--format', help='The format to dump the data in.',
                               choices=['json', 'json-ld', 'turtle'], default='turtle')
    parser_sample.add_argument('--blank-nodes', default='no', type=str, help='use blank nodes in rdf.', choices=["yes", "no"])

    # dump_bel20 command
    parser_dump_ldes = subparsers.add_parser('version_bel20', help='Dumps the BEL 20 LDES collection.')
    parser_dump_ldes.add_argument('--format', help='The format to dump the data in.', choices=['json', 'json-ld', 'turtle'], default='turtle')
    parser_dump_ldes.add_argument('--blank-nodes', default='no', type=str, help='use blank nodes in rdf.', choices=["yes", "no"])
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
            graph.bind("kbolaunch", KBO)
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
            graph.bind("kbolaunch", KBO)
            graph.bind("org", ORG)
            graph.bind("foaf", FOAF)
            graph.bind("vcard", VCARD)
            graph.bind("locn",LOCN)
            graph.bind("legal",LEGAL)
            graph.bind("terms",TERMNAME)
            enterprise.to_rdf(graph, with_blank_nodes=blank_nodes)
            print(graph.serialize(format=format))
            exit()

    # Get one versioned KBO Enterprise Entity
    elif args.command == 'version_sample':
        enterprise_nr = args.enterprise_nr
        format = args.format
        blank_nodes = args.blank_nodes == "yes"
        enterprise = KboGenerator(BASE_PATH, DB_LOCATION).one(enterprise_nr)
        graph = Graph()

        # bind kbolaunch, org, foaf, vard prefix.
        graph.bind("kbolaunch", KBO)
        graph.bind("org", ORG)
        graph.bind("foaf", FOAF)
        graph.bind("vcard", VCARD)
        graph.bind("locn", LOCN)
        graph.bind("legal", LEGAL)
        graph.bind("terms", TERMNAME)
        graph.bind("geo", GEO)

        enterprise.to_rdf_version(graph, with_blank_nodes=False)
        ent_dict = enterprise.to_dict()
        # print(json.dumps(ent_dict, indent=4))
        # print(ent_dict)
        print(graph.serialize(format='turtle'))

    # Get versioned KBO Enterprise Entities
    elif args.command == 'version_dump_ldes':
        enterprises = KboGenerator(BASE_PATH, DB_LOCATION)
        total_records = enterprises.count()
        current_rec = 0
        for enterprise in enterprises.generate():
            current_rec = current_rec + 1
            graph = Graph()
            graph.bind("kbolaunch", KBO)
            graph.bind("org", ORG)
            graph.bind("foaf", FOAF)
            graph.bind("vcard", VCARD)
            graph.bind("locn", LOCN)
            graph.bind("legal", LEGAL)
            graph.bind("terms", TERMNAME)
            graph.bind("geo", GEO)

            enterprise.to_rdf_version(graph, with_blank_nodes=False)
            print(graph.serialize(format='turtle'))
            # print(f"Processing record {current_rec} of {total_records} [{current_rec/total_records*100:.2f}%]\r", end="")
            print(f"Processing record {current_rec} of {total_records} [{current_rec / total_records * 100:.2f}%]")

    #Bel20 companies, data sample
    elif args.command == 'version_bel20':
        total_records = len(BEL_20)
        current_rec = 0
        for enterprise in BEL_20:
             current_rec = current_rec + 1
             enterprise = KboGenerator(BASE_PATH, DB_LOCATION).one(enterprise)
             graph = Graph()

             # bind kbolaunch, org, foaf, vard prefix.
             graph.bind("kbolaunch", KBO)
             graph.bind("org", ORG)
             graph.bind("foaf", FOAF)
             graph.bind("vcard", VCARD)
             graph.bind("locn", LOCN)
             graph.bind("legal", LEGAL)
             graph.bind("terms", TERMNAME)
             graph.bind("geo", GEO)

             enterprise.to_rdf_version(graph, with_blank_nodes=False)
             ent_dict = enterprise.to_dict()
             # print(json.dumps(ent_dict, indent=4))
             # print(ent_dict)

             f = open(f"sample/bel20/{enterprise.enterprise_number}.ttl", "w+")
             f.write(graph.serialize(format='turtle'))
             f.close()
             #print(graph.serialize(format='turtle'))
             print(f"Processing record {current_rec} of {total_records} [{current_rec / total_records * 100:.2f}%]")

