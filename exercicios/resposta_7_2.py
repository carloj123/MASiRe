# if len(parameters) == 1:
#     match = None
#     for sub_token, sub_action, sub_param in special_action_tokens:
#         if len(sub_param) == 1:
#             if sub_token == parameters[0] and sub_action == 'carry' and sub_param[0] == token:
#                 match = [sub_token, sub_action, sub_param]
#                 break
#
#     if match is not None:
#         special_action_tokens.remove(match)
#         if self.agents_manager.get(parameters[0]) is not None:
#             self.agents_manager.add_physical(parameters[0],
#                                              self.agents_manager.get(token))
#             self.agents_manager.edit(parameters[0], 'last_action_result', 'success')
#             self.agents_manager.edit(parameters[0], 'last_action', 'carry')
#             secondary_result = {
#                 'agent': self.agents_manager.get(parameters[0]),
#                 'message': ''
#             }
#         else:
#             self.social_assets_manager.add_physical(parameters[0],
#                                                     self.agents_manager.get(token))
#             self.agents_manager.edit(parameters[0], 'last_action_result', 'success')
#             self.agents_manager.edit(parameters[0], 'last_action', 'getCarried')
#             secondary_result = {
#                 'social_asset': self.social_assets_manager.get(parameters[0]),
#                 'message': ''
#             }
#     else:
#         raise FailedNoMatch('No other agent or social asset wants to carry.')
#
# else:
#     raise FailedWrongParam('More or less than 1 parameter was given.')