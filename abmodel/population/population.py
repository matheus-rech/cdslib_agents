from enum import Enum
from typing import Optional, Literal

from numpy import array, nan_to_num, inf, maximum, floor, setdiff1d
from scipy.spatial import KDTree
from pandas.core.frame import DataFrame
from pandas import concat

from abmodel.utils.execution_modes import ExecutionModes
from abmodel.models.population import Configutarion
from abmodel.models.health_system import HealthSystem
from abmodel.models.base import SimpleGroups
from abmodel.models.disease import SusceptibilityGroups, MobilityGroups
from abmodel.models.disease import NaturalHistory, DiseaseStates
from abmodel.population.initial_arrangement import InitialArrangement
from abmodel.models.mobility_restrictions import MRTracingPolicies
from abmodel.models.mobility_restrictions import GlobalCyclicMR
from abmodel.models.mobility_restrictions import CyclicMRPolicies
from abmodel.models.disease import IsolationAdherenceGroups
from abmodel.agent.neighbors import AgentNeighbors


class EvolutionModes(Enum):
    """
        This class enumerates the evolution modes that can be used in
        the method Population.evolve() and determines if cumulative
        storing data or not.
    """
    steps = "steps"
    cumulative = "cumulative"


class Population:
    """
        TODO: Add brief explanation

        Attributes
        ----------
        TODO

        Methods
        -------
        TODO
    """
    def __init__(
        self,
        configuration: Configutarion,
        health_system: HealthSystem,
        age_groups: SimpleGroups,
        vulnerability_groups: SimpleGroups,
        mr_groups: SimpleGroups,
        susceptibility_groups: SusceptibilityGroups,
        mobility_groups: MobilityGroups,
        disease_groups: DiseaseStates,
        natural_history: NaturalHistory,
        initial_population_setup_list: list[dict],
        mrt_policies: Optional[MRTracingPolicies] = None,
        global_cyclic_mr: Optional[GlobalCyclicMR] = None,
        cyclic_mr_policies: Optional[CyclicMRPolicies] = None,
        isolation_adherence_groups: Optional[IsolationAdherenceGroups] = None,
        execmode: ExecutionModes = ExecutionModes.iterative.value,
        evolmode: EvolutionModes = EvolutionModes.steps.value
    ) -> None:
        """
            Constructor of Population class.

            TODO: Add brief explanation

            Parameters
            ----------
            TODO

            See Also
            --------
            get_disease_groups_alive : TODO complete explanation

            choose_tracing_radius : TODO complete explanation

            Examples
            --------
            TODO: include some examples
        """
        # Store configuration
        self.configuration = configuration
        self.health_system = health_system
        self.age_groups = age_groups
        self.vulnerability_groups = vulnerability_groups
        self.mr_groups = mr_groups
        self.susceptibility_groups = susceptibility_groups
        self.mobility_groups = mobility_groups
        self.disease_groups = disease_groups
        self.natural_history = natural_history
        self.initial_population_setup_list = initial_population_setup_list
        self.mrt_policies = mrt_policies
        self.global_cyclic_mr = global_cyclic_mr
        self.cyclic_mr_policies = cyclic_mr_policies
        self.isolation_adherence_groups = isolation_adherence_groups
        self.execmode = execmode
        self.evolmode = evolmode

        # TODO
        # Handle units

        # =====================================================================
        # Setup internal variables
        self.__get_disease_groups_alive()
        self.__choose_tracing_radius()

        # =====================================================================
        # Initialize population dataframe
        self.__initialize_df()

    @property
    def evolmode(self):
        return self.__evolmode

    @evolmode.setter
    def evolmode(self, value: EvolutionModes):
        self.__evolmode = value

    def __initialize_df(self):
        """
        """
        # =====================================================================
        # Init population dataframe
        self.__df = DataFrame({
            "agent": list(range(self.configuration.population_number))
        })

        # =====================================================================
        # Setup population's initial arrangement
        for initial_population_setup in self.initial_population_setup_list:
            self.__df = InitialArrangement.setup(
                self.__df,
                **initial_population_setup,
                )

        # =====================================================================
        # Store step information in a private attribute
        # for checking purposes
        self.__step = 0

        # Initialize time columns
        self.__df = self.__df.insert(loc=0, column="step", value=self.__step)
        self.__df = self.__df.insert(loc=1, column="datetime",
                                     value=self.configuration.initial_date)

        # =====================================================================
        # Initialize movement related columns
        pass

        # =====================================================================
        # Initialize disease related columns
        pass

        # =====================================================================
        # Initialize disease related columns
        if self.evolmode == EvolutionModes.cumulative.value:
            self.__accumulated_df = self.__df.copy()

    def get_population_df(self):
        """
        """
        return self.__df

    def get_accumulated_population_df(self):
        """
        """
        if self.evolmode == ExecutionModes.cumulative.value:
            return self.__accumulated_df
        else:
            raise ValueError(f"Denied: evolmode == {self.evolmode}")

    def get_units(self):
        """
        """
        return None

    def evolve(
        self,
        iterations: int
    ):
        """
            # TODO: add the option to iterate by date
        """
        for step in range(iterations):
            self.__evolve_single_step()

            if self.evolmode == ExecutionModes.cumulative.value:
                self.__accumulated_df = concat(
                    [self.__accumulated_df, self.__df],
                    ignore_index=True
                    )

    def __evolve_single_step(self):
        """
        """
        # =====================================================================
        # Remove dead agents before evolving population dataframe
        # TODO self.__remove_dead_agents()

        # =====================================================================
        # Evolve step
        self.__step += 1
        self.__df["step"] = self.__step

        # Evolve date
        self.__df["datetime"] += self.configuration.iteration_time

        # =====================================================================
        # Change population states by means of state transition
        # and update diagnosis and hospitalization states
        # TODO

        # =====================================================================
        # Quarantine
        # TODO

        # =====================================================================
        # Create KDTree for agents of each alive disease state
        self.__kdtrees_and_agents_indices()

        # =====================================================================
        # Trace neighbors to susceptible agents
        # self.__df = AgentNeighbors.trace_neighbors_to_susceptibles(
        #     df: DataFrame,
        #     tracing_radius: float,
        #     kdtree_by_disease_state: dict,
        #     agents_labels_by_disease_state: dict,
        #     dead_disease_group: str,
        #     disease_groups: DiseaseStates,
        #     execmode: ExecutionModes = ExecutionModes.vectorized.value
        #     )

        # =====================================================================
        # Update alertness states and avoid avoidable agents
        # TODO

        # =====================================================================
        # Change population states by means of contagion
        # TODO

        # =====================================================================
        # Update agents' positions and velocities
        # TODO

    def __get_disease_groups_alive(self) -> None:
        """
            TODO: Add brief explanation

            Parameters
            ----------
            TODO

            See Also
            --------
            TODO

            Examples
            --------
            TODO: include some examples
        """
        # Retrieve disease group label which corresponds to those dead
        for disease_group_label in self.disease_groups.items.keys():
            if self.disease_groups.items[disease_group_label].is_dead:
                self.dead_disease_group = disease_group_label

        # Also exclude those dead from disease groups alive
        self.disease_groups_alive = list(setdiff1d(
            list(self.disease_groups.items.keys()),
            [self.dead_disease_group]
            ))

    def __choose_tracing_radius(self) -> None:
        """
            TODO: Add brief explanation

            Parameters
            ----------
            TODO

            See Also
            --------
            TODO

            Examples
            --------
            TODO: include some examples
        """
        # Retrieve maximum radius for trace_neighbors function
        spread_radius_list = [
            self.disease_groups.items[disease_group].spread_radius
            for disease_group in self.disease_groups.items.keys()
            ]

        avoidance_radius_list = [
            self.natural_history.items[key].avoidance_radius
            for key in self.natural_history.items.keys()
            ]

        spread_radius_arr = array(spread_radius_list, dtype=float)
        spread_radius_arr = nan_to_num(spread_radius_arr, nan=-inf)
        max_spread_radius = spread_radius_arr.max()

        avoidance_radius_arr = array(avoidance_radius_list, dtype=float)
        avoidance_radius_arr = nan_to_num(avoidance_radius_arr, nan=-inf)
        max_avoidance_radius = avoidance_radius_arr.max()

        self.tracing_radius = maximum(
            max_spread_radius,
            max_avoidance_radius
            )

    def __kdtrees_and_agents_indices(self) -> None:
        """
            TODO: Add brief explanation

            Parameters
            ----------
            TODO

            See Also
            --------
            TODO

            Examples
            --------
            TODO: include some examples
        """
        self.kdtree_by_disease_state = {}
        self.agents_labels_by_disease_state = {}

        for disease_state in self.disease_groups_alive:
            # Filter population
            # Exclude those agents hospitalized and those that are dead
            filtered_df = self.population.loc[
                (self.population["disease_state"] == disease_state)
                &
                (~self.population["is_hospitalized"])
                &
                (~self.population["is_dead"])
                ][["agent", "x", "y"]].copy()

            # Calculate how many points were retrieved
            n_points = filtered_df.shape[0]

            if n_points != 0:
                # Get all agents locations
                locations = filtered_df[["x", "y"]].to_numpy()

                # Get all agents labels
                agents_labels = filtered_df["agent"].to_numpy()

                # Select a sensible leafsize for the KDtree method
                one_percent_of_points = floor(n_points*0.01)
                leafsize = (
                    one_percent_of_points
                    if one_percent_of_points > 10 else 10
                    )

                # Initialize (calculate) tree for the disease state
                # and store it inside the dict kdtree_by_disease_state
                self.kdtree_by_disease_state[disease_state] = KDTree(
                    locations, leafsize=leafsize
                    )

                # Also store the corresponding agents labels
                self.agents_labels_by_disease_state[disease_state] = \
                    agents_labels
            else:
                # n_points == 0
                self.kdtree_by_disease_state[disease_state] = None
                self.agents_labels_by_disease_state[disease_state] = None
