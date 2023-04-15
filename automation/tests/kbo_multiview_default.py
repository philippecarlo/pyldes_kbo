#!/usr/bin/python
import time
import unittest
from rdflib import Graph
from pyldes_kbo.automation.support import Support

su = Support()
url_view_by_page = "http://localhost:8080/kbo/by-page"
url_first_fragment_page = "http://localhost:8080/kbo/by-page?pageNumber=1"
url_random_page_page = "http://localhost:8080/kbo/by-page?pageNumber=5"

url_view_by_page_geo = "http://localhost:8080/kbo/by-location"
url_first_fragment_geo = "http://localhost:8080/kbo/by-location?tile=0/0/0"
url_random_page_geo = "http://localhost:8080/kbo/by-location?tile=15/16778/10945"


url_view_by_page_sub = "http://localhost:8080/kbo/by-name"
url_first_fragment_sub = "http://localhost:8080/kbo/by-name?substring="
url_random_page_sub = "http://localhost:8080/kbo/by-name?substring=b"

docker_compose_file = "../../cegekaKBO/cegeka_kbo_multiview/docker-compose.yml"
data_location = "../../sample/bel20/*"

class TestDefaultMultiview(unittest.TestCase):

    # Pagination view
    def test_1_start_services(self):
        print("######################Multiview defaultPagination: Service starting....###################")
        time.sleep(20)
        su.start_service(path_docker=docker_compose_file)
        time.sleep(100)
        self.assertEqual(su.server_ready().status_code, 200)

    def test_2_post_data(self):
        print("######################Multiview defaultPagination: Data ingesting....###################")
        su.post_data(location=data_location)
        self.assertEqual(su.server_ready().status_code, 200)

    # Verify if the data is properly ingested and the view page is as expected_pagination
    def test_3_verify_view_pagination(self):
        print("######################Multiview defaultPagination: Verify first view....###################")
        graph_expected = Graph().parse('../expected/expected_pagination/view.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_view_by_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    # Verify if the data is properly ingested and first pagination is as expected
    def test_4_verify_fist_page_pagination(self):
        print("######################Multiview defaultPagination: Verify fragments....###################")
        graph_expected = Graph().parse('../expected/expected_pagination/page1.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_first_fragment_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    def test_5_verify_random_page_pagination(self):
        print("######################Multiview defaultPagination: Verify fragments with random page....###################")
        graph_expected = Graph().parse('../expected/expected_pagination/random.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_random_page_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    #Geo View
    def test_6_verify_fist_page_geofragment(self):
        print("######################Multiview defaultGeofragment: Verify fragments....###################")
        graph_expected = Graph().parse('../expected/expected_geofragment/page1.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_first_fragment_geo).content,
                                     format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    def test_7_verify_random_page_geofragment(self):
        print("######################Multiview defaultGeofragment: Verify fragments with random page....###################")
        graph_expected = Graph().parse('../expected/expected_geofragment/random.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_random_page_geo).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))


    #substring View

    def test_8_verify_random_page_substring(self):
        print("#####################Multiview defaultSubstring:Random fragment verify...#############")
        graph_expected = Graph().parse('../expected/expected_substring/random.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_random_page_sub).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    # todo
    # Define a test to verify the integrity of the dataset

    def test_9_tear_down(self):
        print("##################### Tear down....##########################")
        su.stop_server(path_docker=docker_compose_file)
