# info = {'type': 'percepts', 'environment': {}, 'message': ''}
#
#     if response:
#         if response['status']:
#             info['status'] = response['status']
#             info['result'] = True
#
#             found_index = 0
#             for idx, actor in enumerate(response['actors']):
#                 if 'agent' in actor:
#                     if actor['agent']['token'] == token:
#                         info['agent'] = agent_variables(actor['agent'])
#                         info['message'] = actor['message']
#                         found_index = idx
#                         break
#                 else:
#                     if actor['asset']['token'] == token:
#                         info['agent'] = asset_variables(actor['asset'])
#                         info['message'] = actor['message']
#                         found_index = idx
#                         break
#
#             if 'agent' not in info:
#                 return event_error_format('Actor not found in response. ')
#
#             response['actors'].pop(found_index)
#             info['environment'] = response['environment']
#
#         else:
#             event_error_format(response['message'])
#
#         return info
#
#     else:
#         return event_error_format('Empty simulation response. ')