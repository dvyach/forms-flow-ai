"""Test suite for process API endpoint"""
from tests.utilities.base_test import get_token_header, get_token_body


def test_process_get_all_processes(client, session, jwt):
    """Test process get all processes"""
    token = jwt.create_jwt(get_token_body(), get_token_header())
    headers = {"Authorization": f"Bearer {token}", "content-type": "application/json"}
    response = client.get("/application", headers=headers)
    assert response.status_code == 200


# TODO: Add integration test using BPM Mock APIs
# def test_process_xml_details(client, session, jwt):
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrYTFKalB6Vy1EaHNFSE9vd2NZVHRJdW9sR3FqT0NhN1NYV0RFcDI1dGZBIn0.eyJqdGkiOiJjZjBlYjVmZS0zMGE2LTRiY2QtOTM1OS03ZTVjMzg4ZWZjZjAiLCJleHAiOjE2MzYzNTY0MDMsIm5iZiI6MCwiaWF0IjoxNjM1NDkyNDAzLCJpc3MiOiJodHRwczovL2lhbS5hb3QtdGVjaG5vbG9naWVzLmNvbS9hdXRoL3JlYWxtcy9mb3Jtc2Zsb3ctYWktd2lsbG93IiwiYXVkIjpbImNhbXVuZGEtcmVzdC1hcGkiLCJmb3Jtcy1mbG93LXdlYiIsImFjY291bnQiXSwic3ViIjoiMmYzMThhMDktNDY3YS00MTUxLTliMzAtY2Y3NTg4MTlmMDU1IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZm9ybXMtZmxvdy13ZWIiLCJhdXRoX3RpbWUiOjAsInNlc3Npb25fc3RhdGUiOiIwOGEzZTVlMi1lYTZlLTRkYTUtYjQzZi05MTIyYjgwOWNhNDkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJmb3Jtcy1mbG93LXdlYiI6eyJyb2xlcyI6WyJmb3Jtc2Zsb3ctZGVzaWduZXIiXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiY2FtdW5kYS1yZXN0LWFwaSBlbWFpbCBwcm9maWxlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJyb2xlIjpbImZvcm1zZmxvdy1kZXNpZ25lciJdLCJuYW1lIjoiUGV0ZXIgV2F0dHMiLCJncm91cHMiOlsiL2NhbXVuZGEtYWRtaW4iLCIvZm9ybXNmbG93L2Zvcm1zZmxvdy1kZXNpZ25lciJdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwZXRlci13YXR0cyIsImdpdmVuX25hbWUiOiJQZXRlciIsImZhbWlseV9uYW1lIjoiV2F0dHMiLCJlbWFpbCI6InBldGVyLndhdHRzQGFvdC5jb20ifQ.ioYSAO9hgbNl2w7vET9vBFL1DDi1YqX6x0N0HokGZsntNRWLkrh8sawmTnJ3z4ambMmI2Swy9jRiV_GhNjaXy-DzQa8WkHsFZixuiYhNM6KuUypwo49H9JhW9xs9Dyo0ejlL3IkS20yKDHFx69ee0YxFiVtNv8_zdFEn2OOj2zQAVPmfzzcD0GyaAEVKdBhelENYDF4BDNWNO77YfrlYURMcRhtC3ptAm_SbbL05hkGKHVVMWoukgEJ2iH0Y40qEYg8MOGrrDscl2eywpNNqvoxpFPGHjGfM_5wvNnVzhnHc_JBt9mIyNFFuPDzoS9OBVEXuS7DxxiKf8sYrx0LzIQ"
#     }
#     response = client.get("/process/one-step-approval/xml", headers=headers)
#     assert response.status_code == response