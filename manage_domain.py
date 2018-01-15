import manage_requests
import requests
import manage_xml

def get_domain_values(env, domain_name):

    request_specification = f"/rest/service/admin/domains/{domain_name}"
    request = manage_requests.prepare_get_request(env, request_specification)
    get_response = requests.get(request)

    domain_values_list = manage_xml.extract_xml_elements_by_path(get_response.content, './/valueHierarchy')
    domain_values_text_list = list(map(lambda x: x.text, domain_values_list))
    return domain_values_text_list

def get_domain_values_missing_from_list(domain_values, domain_list):

    missing_domain_values = [value for value in domain_values if value not in domain_list]
    return missing_domain_values