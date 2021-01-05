store = {}
store['timestamp']=1609768463
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '2']
store['commit']='808403cd2b48f26a866d0b4014e6ddacd13301f8'
store['github_url']='808403cd2b48f26a866d0b4014e6ddacd13301f8'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=120
store['config']={'seed': 2, 'acquisition_size': 10, 'max_training_set': 300, 'num_pool_samples': 100, 'num_eval_samples': 4, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 24576, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.batchbaldical'}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.518310546875, 'crossentropy': 6.608333393931389})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.52392578125, 'crossentropy': 7.051165126264095})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.519287109375, 'crossentropy': 7.453102521598339})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.506591796875, 'crossentropy': 5.973579194396734})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.53466796875, 'crossentropy': 6.755846783518791})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.53662109375, 'crossentropy': 6.380495168268681})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.526611328125, 'crossentropy': 6.432551629841328})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.514, 'crossentropy': 5.6608857139587405}
store['active_learning_steps'][0]['pool_training']={}
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 413, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 328, in run\n    pool_model = self.train_pool_model(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 224, in train_pool_model\n    log_probs_N_C = get_predictions(model=eval_model, loader=train_pool_loader, device=self.device).cpu()\n  File "/scratch-ssd/andsch/conda_envs/job-48131/lib/python3.8/site-packages/torch/autograd/grad_mode.py", line 26, in decorate_context\n    return func(*args, **kwargs)\nTypeError: get_predictions() missing 2 required keyword-only arguments: \'num_samples\' and \'num_classes\'\n'