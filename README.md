### Background
This repo serves to make writing unit tests for GQL queries faster.

In the typical Graphiql workflow, testing is done in Graphiql first until it works. 

From here, the code is ported over to unit-tests in individual repos to be repeated.

Porting over to unit test takes time because of nitty bitty details like converting camelcase to snake and formatting variables to be used with graphene.

### Steps to use

> pipenv install

Paste your `variables` in Graphiql into the `input.json` file.

> pipenv run python dev.py

Your variables that are formatted nicely for unit-tests are 
found in `tmp/output.py`

