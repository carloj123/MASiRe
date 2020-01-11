# sim_response = requests.post(f'http://{base_url}:{simulation_port}/register_agent',
#                              json={'token': message, 'secret': secret}).json()
#
# if sim_response['status'] == 1:
#     Logger.normal('Agent socket connected.')
#
#     response['status'] = 1
#     response['result'] = True
#     response['message'] = 'Agent successfully connected.'
#
#     response.update(sim_response)
#
#     if controller.agents_amount == len(controller.manager.agents_sockets_manager.get_tokens()):
#         every_agent_registered.put(True)
#
#         one_agent_registered_queue.put(True)
#
#         send_initial_percepts(message, response)
#
#         else:
#         Logger.error(f'Error to connect the agent socket: {message}')
#
#         response['status'] = sim_response['status']
#         response['message'] = sim_response['message']