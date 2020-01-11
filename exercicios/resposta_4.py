# controller.set_processing_actions()
# notify_monitor(percepts_event, sim_response)
#
# if sim_response['status'] == 2:
#     Logger.normal('Open connections for the social assets.')
#
#     controller.asset_request_manager.start_new_asset_request(sim_response)
#     multiprocessing.Process(target=step_controller, args=(request_queue, 2), daemon=True).start()
#
# else:
#     notify_actors(percepts_event, sim_response)
#     Logger.normal('Wait all the agent send yours actions.')
#
#     multiprocessing.Process(target=step_controller, args=(actions_queue, 1), daemon=True).start()