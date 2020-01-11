# token, action, parameters = token_action_param.values()
#
#             if action in special_actions:
#                 special_action_tokens.append([token, action, parameters])
#                 continue
#
#             if token in agents_tokens:
#                 result = self._execute_agent_action(token, action, parameters)
#
#                 if action in requests_action and not result['message']:
#                     requests.append(token)
#
#                 action_results.append(result)
#                 agents_tokens.remove(token)
#
#             else:
#                 action_results.append(self._execute_asset_action(token, action, parameters))
#                 assets_tokens.remove(token)