import json
import argparse
from rdflib import Graph, ORG, FOAF, SKOS
from namespace.kbo import KBO
from namespace.vcard import VCARD
from namespace.geo import GEO
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the KBO example.')
    parser.add_argument('command', type=str, choices=['load', 'run', 'sample','version_sample','version_run','version_bel20'], help='Command to run')
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
        enterprise = KboGenerator(BASE_PATH, DB_LOCATION).one("0416.822.559")
        graph = Graph()

        #bind kbo, org, foaf, vard prefix.

        graph.bind("kbo", KBO)
        graph.bind("org", ORG)
        graph.bind("foaf", FOAF)
        graph.bind("vcard", VCARD)
        graph.bind("locn",LOCN)
        graph.bind("legal",LEGAL)
        graph.bind("terms",TERMNAME)
        graph.bind("geo", GEO)

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
        graph.bind("geo", GEO)

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

             # bind kbo, org, foaf, vard prefix.
             graph.bind("kbo", KBO)
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

             f = open(f"data/Output/{enterprise.enterprise_number}.ttl", "w+")
             f.write(graph.serialize(format='turtle'))
             f.close()
             #print(graph.serialize(format='turtle'))
             print(f"Processing record {current_rec} of {total_records} [{current_rec / total_records * 100:.2f}%]")