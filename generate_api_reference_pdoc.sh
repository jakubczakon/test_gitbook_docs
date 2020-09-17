pdoc /home/jakub/miniconda3/envs/neptune_docs/lib/python3.6/site-packages/neptune \
-o  api-reference/ \
--config 'docformat="google"' \
--force --skip-errors --html

pdoc /home/jakub/miniconda3/envs/neptune_docs/lib/python3.6/site-packages/neptunecontrib \
-o  api-reference/ \
--config 'docformat="google"' \
--force --skip-errors --html

pdoc /home/jakub/miniconda3/envs/neptune_docs/lib/python3.6/site-packages/optuna \
-o  api-reference/ \
--config 'docformat="google"' \
--force --skip-errors --html
