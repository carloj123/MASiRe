# based on https://github.com/agentcontest/massim/blob/master/server/src/main/java/massim/scenario/city/data
# /WorldState.java
import random
from src.simulation.simulated_enviroment.environment_executors.action_executor import ActionExecutor
from src.simulation.simulated_enviroment.environment_variables.agent import Agent
from src.simulation.simulated_enviroment.environment_variables.role import Role
from src.simulation.simulated_enviroment.environment_executors.generator import Generator
from src.simulation.simulated_enviroment.environment_executors.cdm import Cdm


class World:

    def __init__(self, config):
        """
        [Object that represents the simulation universe.]

        :param config: The configuration archive received by the
        communication core.
        """
        self.config = config
        self.events = []
        self.roles = {}
        self.agents = {}
        self.active_events = []
        self.floods = []
        self.water_samples = []
        self.photos = []
        self.victims = []
        self.cdm = Cdm([config['map']['centerLat'], config['map']['centerLon']])
        self.generator = Generator(config)
        self.action_executor = ActionExecutor(config, self)

    def percepts(self, step):
        """
        [Method that generates each step's percepts.]
        
        :param step: The step number the simulation is in
        :return: Three lists, each one containing information about
        the active events of the simulation and one Flood object
        """
        if self.events[step] is None:
            return []

        else:
            flood = self.events[step]
            water_samples = [water_sample for water_sample in self.events[step].water_samples if water_sample.active]
            photos = [photo for photo in self.events[step].photos if photo.active]
            victims = [victim for victim in self.events[step].victims if victim.active]
            return flood, water_samples, photos, victims

    def generate_events(self):
        """
        [Method that generates the world's random events and 
        adds them to their respective category.]
        """
        self.events = self.generator.generate_events()

        for flood in self.events:
            if flood is None:
                continue

            self.floods.append(flood)
            for water_sample in flood.water_samples:
                self.water_samples.append(water_sample)

            for photo in flood.photos:
                if photo is not None:
                    self.photos.append(photo)
                    for victim in photo.victims:
                        self.victims.append(victim)

    def create_roles(self):
        """
        [Method that generates the agent's roles.]
        """
        for role in self.config['roles']:
            self.roles[role] = Role(role, self.config['roles'])

    def create_agent(self, token):
        """
        [Method creates list containing each role times the amount of agents
        it should have and assign one randomly chosen role to the given token]

        :return: A agent containing all the information recovered from the role
        """
        roles = []
        for role in self.config['agents']:
            role = [role] * self.config['agents'][role]
            roles.extend(role)

        role = random.choice(roles)
        agent = Agent(token, self.roles[role], role)
        self.agents[token] = agent
        return agent

    def execute_actions(self, actions):
        """
        [Method that parses all the actions recovered from the communication core
        and calls its execution during a step.]
        
        :param actions: A json file sent by the communication core
        containing all the actions, including the necessary parameters,
        and its respective agents.
        :return: A list containing every agent's action result,
        marking it with a success or failure flag.
        """
        return self.action_executor.execute_actions(actions)

    def create_route_coordinate(self, start, location):
        # create route between location START and LOCATION
        # both are a list -> [lat, long]

        # self.router.
        return
