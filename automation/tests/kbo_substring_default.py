#!/usr/bin/python
import time
import unittest
from rdflib import Graph
from pyldes_kbo.automation.support import Support

su = Support()
url_view_by_page = "http://localhost:8080/kbo/by-name"
url_first_fragment = "http://localhost:8080/kbo/by-name?substring="
url_random_page = "http://localhost:8080/kbo/by-name?substring=b"
docker_compose_file = "../../cegekaKBO/cegeka_kbo_substring/docker-compose.yml"
data_location = "../../sample/bel20/*"


class TestDefaultSubstring(unittest.TestCase):
    def test_1_start_services(self):
        print("#####################defaultSubstring:Service starting....##########################")
        time.sleep(20)
        su.start_service(path_docker=docker_compose_file)
        time.sleep(100)
        self.assertEqual(su.server_ready().status_code, 200)

    def test_2_post_data(self):
        print("#####################defaultSubstring:Data ingesting....##########################")
        su.post_data(location=data_location)
        self.assertEqual(su.server_ready().status_code, 200)

    # Verify if the data is properly ingested and the view page is as expected_pagination
    def test_3_verify_view(self):
        print("#####################defaultSubstring:View verify..")
        graph_expected = Graph().parse('../expected/expected_substring/view.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_view_by_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    # Verify if the data is properly ingested and first pagination is as exepcted
    # def test_4_verify_fist_page(self):
    #     print("#####################defaultSubstring:View verify..")
    #     graph_expected = Graph().parse('../expected/expected_substring/page1.turtle', format='turtle')
    #     graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_first_fragment).content, format='json-ld')
    #     self.assertTrue(graph_expected.isomorphic(graph_actual))

    def test_5_verify_random_page(self):
        print("#####################defaultSubstring:Random fragment verify...#############")
        graph_expected = Graph().parse('../expected/expected_substring/random.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_random_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    # todo
    # Define a test to verify the integrity of the dataset

    def test_6_tear_down(self):
        print("#####################defaultSubstring:Tear down....##########################")
        su.stop_server(path_docker=docker_compose_file)
