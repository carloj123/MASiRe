# self.map.restart(config['map']['maps'][0], config['map']['proximity'], config['map']['movementRestrictions'])
#
# if load_sim:
#     generator = Loader(config)
# else:
#     generator = Generator(config, self.map)
#
# self.steps = generator.generate_events()
# self.social_assets_manager = SocialAssetsManager(config['map'], config['socialAssets'],
#                                                  generator.generate_social_assets())
#
# if write_sim:
#     self.write_match(generator, self.sim_file)
#
# self.map_percepts = config['map']
# self.max_floods = generator.flood_id
# self.max_victims = generator.victim_id
# self.max_photos = generator.photo_id
# self.max_water_samples = generator.water_sample_id
# self.delivered_items = []
# self.current_step = 0
# self.max_steps = config['map']['steps']
# self.cdm_location = (config['map']['maps'][0]['centerLat'], config['map']['maps'][0]['centerLon'])
# self.agents_manager.restart(config['agents'], self.cdm_location)