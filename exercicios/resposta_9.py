# response = {'status': 0, 'result': False, 'message': ''}
#
# if not controller.simulation_started():
#     response['message'] = 'The simulator has not started yet.'
#
# else:
#     status, message = controller.check_service_request(request)
#
#     if status == 1:
#         # Can be add more types of services
#         sim_response = requests.get(f'http://{base_url}:{simulation_port}/calculate_route',
#                                     json={'parameters': request.get_json(force=True)['parameters'],
#                                           'secret': secret}).json()
#
#         if sim_response['status'] == 1:
#             response['status'] = 1
#             response['result'] = True
#             response['response'] = sim_response['response']
#         else:
#             response['message'] = sim_response['message']
#     else:
#         response['message'] = message
#
# return jsonify(response)