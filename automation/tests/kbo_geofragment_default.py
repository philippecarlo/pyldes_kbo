#!/usr/bin/python
import unittest
from pyldes_kbo.automation.support import Support
import time
from rdflib import Graph

su = Support()
url_view_by_page = "http://localhost:8080/kbo/by-location"
url_first_fragment = "http://localhost:8080/kbo/by-location?tile=0/0/0"
url_random_page = "http://localhost:8080/kbo/by-location?tile=15/16778/10945"
docker_compose_file = "../../cegekaKBO/cegeka_kbo_geofragment/docker-compose.yml"
data_location = "../../sample/bel20/*"


class TestDefaultGeoFragment(unittest.TestCase):
    def test_1_start_services(self):
        print("######################defaultGeofragment: Service starting....###################")
        su.start_service(path_docker=docker_compose_file)
        time.sleep(60)
        self.assertEqual(su.server_ready().status_code, 200)

    def test_2_post_data(self):
        print("######################defaultGeofragment: Data ingesting....###################")
        su.post_data(location=data_location)
        self.assertEqual(su.server_ready().status_code, 200)

    # Verify if the data is properly ingested and the view page is as expected_geofragment
    def test_3_verify_view(self):
        print("######################defaultGeofragment: Verify first view....###################")
        graph_expected = Graph().parse('../expected/expected_geofragment/view.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_view_by_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    # Verify if the data is properly ingested and first pagination is as exepcted
    def test_4_verify_fist_page(self):
        print("######################defaultGeofragment: Verify fragments....###################")
        graph_expected = Graph().parse('../expected/expected_geofragment/page1.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_first_fragment).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    def test_5_verify_random_page(self):
        print("######################defaultGeofragment: Verify fragments with random page....###################")
        graph_expected = Graph().parse('../expected/expected_geofragment/random.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_random_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    # todo
    # Define a test to verify the integrity of the dataset

    def test_6_tear_down(self):
        print("######################defaultGeofragment: Tear down....###################")
        su.stop_server(path_docker=docker_compose_file)

# if __name__ == '__main__':
#          Support().post_data(location= "../../sample/bel20/*")
