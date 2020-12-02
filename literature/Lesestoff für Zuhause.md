# Software Engineering für Data Analytics

## Dependency Management, Virtual Environment

- ! https://www.youtube.com/watch?v=-C8uVImkTQg

- virtual environment
- dependency management, package installation
- distribution
- repository
- venv
- pip, pypi
- conda, anaconda

## Python Programming

- Was sind Python Module?
- Functionen
- Module
- Method types: staticmethod, classmethod, normal method
- Seiteeffekt / Pure functionen
- API: https://en.wikipedia.org/wiki/API

## ! Refactoring

- http://nathanmarz.com/blog/suffering-oriented-programming.html
- https://martinfowler.com/articles/workflowsOfRefactoring
- https://martinfowler.com/books/refactoring.html
- Rapid Prototyping: https://de.wikipedia.org/wiki/Rapid_Prototyping
- Refactoring: https://refactoring.com/

- agiles manifest
- scrum
- kanban

Fail Fast:
1. Im Program
2. Im Project
3. Im Business / Startup

## ! Code Smell

- https://refactoring.guru/refactoring/smells
- https://www.martinfowler.com/bliki/CodeSmell.html
- https://hilton.org.uk/blog/naming-smells
- https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/
- Camel-case, snake-case

## ! Git

- https://www.atlassian.com/de/git/tutorials
- https://chris.beams.io/posts/git-commit/

## Test driven development

- Test driven development
- Behaviour driven development

## ! Python for Analytics

### Plotnine und ggplot2 (aber für R)

- https://plotnine.readthedocs.io/en/stable/
- https://github.com/has2k1/plotnine
- https://ggplot2.tidyverse.org/

### Dplyr, plydata, dfply

- https://dplyr.tidyverse.org/
- https://github.com/has2k1/plydata
- https://github.com/kieferk/dfply

### !! Libraries, Frameworks, Inversion of control

- library
- framework
- inversion of control: https://en.wikipedia.org/wiki/Inversion_of_control
- Boilerplate code: https://en.wikipedia.org/wiki/Boilerplate_code
- What is the difference between a framework and a library? (sehr kurz) https://www.youtube.com/watch?v=D_MO9vIRBcA
- See below for "framework" in the context of data science, instead of software engineering. But the two are very similar.

### Developing scikit-learn BaseEstimator and Mixins

- https://scikit-learn.org/stable/modules/classes.html#base-classes
- https://scikit-learn.org/stable/developers/develop.html
- https://stackoverflow.com/questions/63341996/implement-a-scikit-learn-meta-estimator-with-unknown-interface-of-the-respective

--------------------------------------------------------------------

## Documentation in Python

### docstring in Python

- https://stackoverflow.com/questions/11163436/are-there-any-real-alternatives-to-restructuredtext-for-python-documentation
- https://stackoverflow.com/questions/23954109/difference-between-and-nothing-in-python-docstrings
- https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
- https://bwanamarko.alwaysdata.net/napoleon/format_exception.html
- https://www.python.org/dev/peps/pep-0257/
- http://daouzli.com/blog/docstring.html

### numpydoc

- https://codeandchaos.wordpress.com/2012/08/09/sphinx-and-numpydoc/
- http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
- https://numpydoc.readthedocs.io/en/latest/format.html

### docstrings in PyCharm

- https://www.jetbrains.com/help/pycharm/creating-documentation-comments.html
- https://stackoverflow.com/questions/18666885/custom-pycharm-docstring-stubs-i-e-for-google-docstring-or-numpydoc-formats
- https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000784410-how-to-change-pycharm-default-commenting-style-for-function-

--------------------------------------------------------------------

# !! Data Science

*Methodologie* = eine Lehre über Methoden:
- https://en.wikipedia.org/wiki/Methodology
- Beispiel: Unterricht von Richard Leibrandt

*Methodik* = Menge von Methoden, die das selbe Ziel hat.
- Beispiel: Klassierung

*Methode* = Vorgehensweise, die für sich alleine stehen kann. Eine Methode muss nicht endlich sein (in Speicher oder Zeit). Dabei muss nicht jeder Aspekt vollständig definiert sein. Schritte können Methodiken sein, was eine Methode zu einem Framework macht. Schritte einer Methode können weitere Methoden oder Methodiken sein.
- Beispiel: Entscheidungsbaum
- https://en.wikipedia.org/wiki/Software_framework (Anfang)

*Framework* = method which leaves certain steps open by just defining what the goal is. Such a step is a Methodik.

*Technique* = Vorgehensweise, die eingebaut werden kann in eine Methode oder mit einer Method kombiniert werden kann um eine andere Methode zu ergeben. Kann nicht für sich alleine stehen und kann keinen Algorithmus ergeben.
- Beispiel: Kernel Trick

*Algorithm* = Methode, die implementiert werden kann.
- Beispiel: xgboost
- https://de.wikipedia.org/wiki/Algorithmus#Eigenschaften (diesen Abschnitt)

*Program* = implementiert einen Algorithmus (im Kontext von Data Analytics).
- Beispiel: xgboost implemented in Python

*Data Analytics* = the discipline that applies data science principles to concrete problems

----------------------------------

## !! Übersicht Mathematik und Informatik

Data Science baut als Wissenschaft auf Mathematik und Informatik auf: 
- Maps of mathematics: https://i.pinimg.com/originals/19/11/cf/1911cf883961eec7b5480e104ff85e04.jpg
- Maps of mathematics: https://www.youtube.com/watch?v=OmJ-4B-mS-Y
- Map of computer science: https://iibawards-prod.s3.amazonaws.com/projects/images/000/002/333/large.png?1505504208
- Map of computer science: https://www.youtube.com/watch?v=SzJ46YA_RaA

----------------------------------

## !! Datasets and spaces

A dataset is a set https://en.wikipedia.org/wiki/Set_(mathematics) or a multiset https://en.wikipedia.org/wiki/Multiset
An element of a dataset can be called a data object.
We can only reason about data objects with the dataset is an underlying set of a mathematical space https://en.wikipedia.org/wiki/Space_(mathematics).
A space is a set together with an added geometrical structures.
Elements of a the underlying set of a space are called "points", that is why you see "data points" sometimes.
Because sometimes the space is a vector space, the respective data objects are called "data vectors".
Two important spaces for data science are the Euclidean space and the metric space.

Data objects might be collection from multiple values, possibly from different levels of levels of measurements: https://en.wikipedia.org/wiki/Level_of_measurement

When we do data analytics, we map (=transform) data object from one space into another space.
The directed acyclic graph (DAG, https://en.wikipedia.org/wiki/Directed_acyclic_graph) that is engineered is sometimes called the *dataflow*.
Datasets are edges of the DAG, transformations/maps are the nodes of the DAG, sometimes called *components*.
From this perspective, "training" is "finding out how to map" and applying a transformation or a machine learning model is doing the map.

"Training" is a function that get the *model structure* and the training data as inputs and outputs the trained model.
The training is often a mathemathical optimization (https://en.wikipedia.org/wiki/Mathematical_optimization), where the model parameters are optimized.
The training model is also known as the fitted model, because the model parameters have been fit to the training data.
The trained model is a function, thus the training is a function that outputs a function.
This last function used during model application to transform datasets to datasets (more an analytics perspective) or maps spaces to spaces (more a data science perspective).

However, we could also have a different view:
We could say that the training is not outputting a function, but "only" the fitted model parameters, which are an input to the model application function.
(Here, the model structure might not be considered to be input, but part of the training algorithm and also part of the model application function. Now only "classical" datasets are moved in the DAG, and we get the name "dataflow".)

Strictly speaking we have three DAG / flows:

1. The DAG that describes the entire technical software product. Here not only datasets are moved from node to node, but also functions (e.g. from training - at least in the first view).
2. The DAG that describes not all aspects of that first DAG, and focus on nodes that map spaces to spaces. This is more helpful during conceptualization. Here we usually omit things like training, or dataset splits (e.g. for training, testing, etc.).
3. The DAG that describes the work that the humand developer does.

----------------------------------

## Optimization

There are two general types of optimization methods:

1. Algorithms which can give guarantees, e.g. https://en.wikipedia.org/wiki/Gradient_descent
2. Heuristics

(But I am not aware of a good definition. It might be that - in the future - I might get to the conclusion that there is no way to differentiate between the two with actual definitions.)

A meta-heuristic is a framework that allows for the development of specific heurstics, e.g. https://en.wikipedia.org/wiki/Simulated_annealing

----------------------------------

## ! Wichtige Methodiken

- Anomaly Detection: Outlier Detection, Novelty Detection
- Classification: https://de.wikipedia.org/wiki/Klassifizierung
- Clustering: https://scikit-learn.org/stable/modules/clustering.html
- Density Estimation
- Imputation: Missing Value Imputation, Anomaly Imputation
- Manifold Learning & Embedding
- Regression, Curve-Fitting, Interpolation, Extrapolation
- Vector Quanization
- Feature Selection

----------------------------------

## Methoden (Beispiele)

### xgboost

- https://www.analyticsvidhya.com/blog/2017/06/which-algorithm-takes-the-crown-light-gbm-vs-xgboost/
- https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/
- https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/
- https://xgboost.readthedocs.io/en/latest/tutorials/model.html
- https://en.wikipedia.org/wiki/Bootstrap_aggregating
- https://en.wikipedia.org/wiki/Ensemble_learning#Common_types_of_ensembles
- https://en.wikipedia.org/wiki/Boosting_(machine_learning)
- https://www.analyticsvidhya.com/blog/2015/05/boosting-algorithms-simplified/
- https://en.wikipedia.org/wiki/AdaBoost
- https://towardsdatascience.com/catboost-vs-light-gbm-vs-xgboost-5f93620723db
- https://medium.com/@pushkarmandot/https-medium-com-pushkarmandot-what-is-lightgbm-how-to-implement-it-how-to-fine-tune-the-parameters-60347819b7fc
- https://github.com/microsoft/LightGBM/tree/master/python-package
- https://lightgbm.readthedocs.io/en/latest/index.html
- https://github.com/microsoft/LightGBM
- https://www.kaggle.com/ezietsman/simple-python-lightgbm-example
- https://www.quora.com/Which-models-outperform-XGBoost-and-help-win-Kaggle-competitions#
- https://medium.com/data-design/xgboost-hi-im-gamma-what-can-i-do-for-you-and-the-tuning-of-regularization-a42ea17e6ab6
- https://towardsdatascience.com/fine-tuning-xgboost-in-python-like-a-boss-b4543ed8b1e
- https://xgboost.readthedocs.io/en/latest/python/python_api.html
- https://stackoverflow.com/questions/34674797/xgboost-xgbclassifier-defaults-in-python

----------------------------------

## Wichtige Techniken

### Regularization

- https://towardsdatascience.com/regularization-for-machine-learning-models-9173c2e90449
- https://www.machinecurve.com/index.php/2020/01/21/what-are-l1-l2-and-elastic-net-regularization-in-neural-networks/#elastic-net-regularization

### Calibration

- https://scikit-learn.org/stable/modules/calibration.html

### Forensic

### Hyperparameter Tuning/Optimization (of Regularization)

- https://scikit-learn.org/stable/modules/grid_search.html
- https://github.com/hyperopt/hyperopt
- https://stackoverflow.com/questions/52580023/how-to-get-the-best-estimator-parameters-out-from-pipelined-gridsearch-and-cro
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
- https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html
- https://towardsdatascience.com/random-search-vs-grid-search-for-hyperparameter-optimization-345e1422899d
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html
- https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html

--------------------------------------------------------------------

# Angewandte Themen

- Forensic

## Missing Values

- http://www.theanalysisfactor.com/mar-and-mcar-missing-data/
- http://www.theanalysisfactor.com/missing-data-mechanism/
- https://stats.stackexchange.com/questions/103500/machine-learning-algorithms-to-handle-missing-data

## Imbalanced datasets

- https://pypi.org/project/imbalanced-learn/
- https://www.kdnuggets.com/2019/11/tips-class-imbalance-missing-labels.html

## Model Selection

- https://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html
- https://stackoverflow.com/questions/38555650/try-multiple-estimator-in-one-grid-search

--------------------------------------------------------------------

# Hintergründe

## AI Winter

- https://en.wikipedia.org/wiki/AI_winter
- https://blog.piekniewski.info/2018/05/28/ai-winter-is-well-on-its-way/

----------------------------------

## Geschäftsmodelle in AI

- https://medium.com/thelaunchpad/your-deep-learning-tools-for-enterprises-startup-will-fail-94fb70683834
