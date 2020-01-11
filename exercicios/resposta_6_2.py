# if monitor_manager.check_match_id(match):
#     if id_attribute == 'report':
#         report = monitor_manager.get_match_report(match)
#
#         if report:
#             return report, 200
#
#         abort(404, message=f'The Match report {match} is not available yet.')
#     elif id_attribute == 'map':
#         map_config = monitor_manager.get_match_map(match)
#
#         if map_config:
#             return map_config, 200
#
#         abort(404, messsage=f'The Match {match} doesnt have map information yet.')
#
#     else:
#         abort(404, message=f'Attribute {id_attribute} is not a valid attribute.')
# abort(404, message=f'Match not found.')