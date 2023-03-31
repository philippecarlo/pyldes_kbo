#!/usr/bin/python
import unittest
from pyldes_kbo.automation.support import Support
import time
from rdflib import Graph, Literal, URIRef

su = Support()
url_view_by_page = "http://localhost:8080/kbo/by-page"
url_first_fragment = "http://localhost:8080/kbo/by-page?pageNumber=1"
url_random_page = "http://localhost:8080/kbo/by-page?pageNumber=5"
docker_compose_file = "../../cegekaKBO/cegeka_kbo_pagination/docker-compose.yml"
data_location = "../../sample/bel20/*"

class TestDefaultPagination(unittest.TestCase):
    def test_1_start_services(self):
        su.start_service(path_docker = docker_compose_file)
        time.sleep(60)
        self.assertEqual(su.server_ready().status_code, 200)

    def test_2_post_data(self):
        su.post_data(location=data_location)
        self.assertEqual(su.server_ready().status_code, 200)

    #Verify if the data is properly ingested and the view page is as expected_pagination
    def test_3_verify_view(self):
        graph_expected = Graph().parse('../expected/expected_pagination/view.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view= url_view_by_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    # Verify if the data is properly ingested and first pagination is as exepcted
    def test_4_verify_fist_page(self):
        graph_expected = Graph().parse('../expected/expected_pagination/page1.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_first_fragment).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    def test_5_verify_random_page(self):
        graph_expected = Graph().parse('../expected/expected_pagination/random.turtle', format='turtle')
        graph_actual = Graph().parse(su.retrieve_specific_page(url_view=url_random_page).content, format='json-ld')
        self.assertTrue(graph_expected.isomorphic(graph_actual))

    #todo
    #Define a test to verify the integrity of the dataset

    def test_6_tear_down(self):
         su.stop_server(path_docker = docker_compose_file)

# if __name__ == '__main__':
#          Support().post_data(location= "../../sample/bel20/*")