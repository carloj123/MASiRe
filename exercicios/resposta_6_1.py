#
# tokens = [*controller.manager.agents_sockets_manager.get_tokens(), *controller.manager.assets_sockets_manager.get_tokens()]
# room_response_list = []
#
# for token in tokens:
#     if event == initial_percepts_event:
#         info = json_formatter.initial_percepts_format(response, token)
#
#     elif event == percepts_event:
#         info = json_formatter.percepts_format(response, token)
#
#     elif event == end_event:
#         info = json_formatter.end_format(response, token)
#
#     elif event == bye_event:
#         info = json_formatter.bye_format(response, token)
#
#     else:
#         Logger.error('Wrong event name. Possible internal errors.')
#         info = json_formatter.event_error_format('Error in API.')
#
#     room = controller.manager.get(token, 'socket')
#     room_response_list.append((room, json.dumps(info)))
#
# for room, agent_response in room_response_list:
#     socket.emit(event, agent_response, room=room)