import itertools
import math
from typing import Optional, Type

import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

from src.module.base_model import BaseModel


class GridSearch:
    """
    A simple grid search class for hyperparameter tuning.

    This class facilitates the search for the best hyperparameters
    given a parameter grid and an estimator
    with a create_variables method.

    Attributes
    ----------
    param_grid : (dict)
        A dictionary where the key is the parameter name
        and the value is a list of values for that parameter.
    verbose : (bool, optional, default True)
        Determines whether to print detail information.
    is_heatmap : (bool, optional, default False)
        Determines whether to plot a heatmap for the scores.
    """

    def __init__(
        self,
        param_grid: dict[str, list],
        verbose: bool = True,
        is_heatmap: bool = False,
    ) -> None:
        self.param_grid = param_grid
        self.verbose = verbose
        self.is_heatmap = is_heatmap
        self.keys = list(param_grid.keys())
        self.values = list(param_grid.values())
        self.params_product = list(itertools.product(*self.values))

    def fit(self, estimator: Type[BaseModel], variables: dict) -> None:
        """
        Fit the estimator given the parameter grid and variables.

        Parameters
        ----------
        estimator : (object)
            The estimator to be tuned.
            It should have a create_variables method.
        variables : (dict)
            Variables to be used in the create_variables method.
        """
        self.__initialize()
        for params in self.params_product:
            self.__train_and_evaluate(estimator, params, variables)
        self.__print_best()
        if self.is_heatmap:
            self.__plot_heatmaps()

    def __initialize(self) -> None:
        """
        Initialize the internal states for the grid search.
        """
        self.score_max = 0.0
        self.best_params: Optional[dict] = None
        if self.is_heatmap:
            self.score_grids = {
                combination: np.zeros(
                    (
                        len(self.param_grid[combination[0]]),
                        len(self.param_grid[combination[1]]),
                    )
                )
                for combination in itertools.combinations(self.keys, 2)
            }

    def __train_and_evaluate(
        self, estimator: Type[BaseModel], params: tuple, variables: dict
    ) -> None:
        """
        Train and evaluate the estimator given the parameters and variables.

        Parameters
        ----------
        estimator : (object)
            The estimator to be tuned.
        params : (tuple)
            Tuple of parameter values.
        variables : (dict)
            Variables to be used in the create_variables method.
        """
        params_dict = dict(zip(self.keys, params))
        _estimator = estimator(**params_dict)
        X, y = _estimator.create_variables(**variables)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )
        _estimator.fit(X_train, y_train)
        score = _estimator.score(X_test, y_test)

        if self.is_heatmap:
            self.__update_score_grids(score, params_dict)
        if score > self.score_max:
            self.score_max = score
            self.best_params = params_dict

    def __update_score_grids(self, score: float, params_dict: dict) -> None:
        """
        Update the score grids with the given score and parameter dictionary.

        Parameters
        ----------
        score : (float)
            Score of the estimator.
        params_dict : (dict)
            Parameter dictionary used for the estimator.
        """
        for combination in itertools.combinations(self.keys, 2):
            self.score_grids[combination][
                self.param_grid[combination[0]].index(
                    params_dict[combination[0]]
                ),
                self.param_grid[combination[1]].index(
                    params_dict[combination[1]]
                ),
            ] = score

    def __print_best(self) -> None:
        """
        Print the best score and parameters if verbose is True.
        """
        if self.verbose:
            print(self.score_max)
            print(self.best_params)

    def __plot_heatmaps(self) -> None:
        """
        Plot heatmaps of scores if is_heatmap is True.
        """
        combinations = list(itertools.combinations(self.keys, 2))
        num_combinations = len(combinations)
        num_rows = int(math.sqrt(num_combinations))
        num_cols = num_combinations // num_rows + (
            num_combinations % num_rows > 0
        )

        fig, axes = plt.subplots(
            num_rows, num_cols, figsize=(5 * num_cols, 5 * num_rows)
        )
        if num_rows == 1 and num_cols == 1:
            axes = np.array([axes])
        else:
            axes = axes.flatten()

        for idx, combination in enumerate(combinations):
            ax = axes[idx]
            sns.heatmap(
                self.score_grids[combination],
                cmap="coolwarm",
                annot=True,
                xticklabels=self.param_grid[combination[1]],
                yticklabels=self.param_grid[combination[0]],
                ax=ax,
            )
            ax.set_xlabel(combination[1])
            ax.set_ylabel(combination[0])

        fig.suptitle("Heatmaps of scores")
        plt.tight_layout()
        plt.show()
